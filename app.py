from datetime import datetime
import os
from sqlalchemy.orm import Session
from flask_migrate import Migrate
from flask import Flask, render_template, request, send_file, redirect
from flask_sqlalchemy import SQLAlchemy
# from mysql import connector
import openai
import elevenlabs
import pygame

app = Flask(__name__, template_folder='templates')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/aistorywritter'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/storyGenText'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db=db)
session = Session()

is_speaking = False

EXPECTATION_WORDS = '750'

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_name = db.Column(db.String(255))
    file = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    age = db.Column(db.Integer)
    language = db.Column(db.String(50))
    mp3_file = db.Column(db.LargeBinary)

    def __repr__(self) -> str:
        return f'{self.id}-{self.story_name}'

# API_KEY_1 = os.environ['secret_key']
API_KEY_1 = open("secret_key.txt", "r").read()
openai.api_key = API_KEY_1

# API_KEY_2 = os.environ['elevenLabs_key']
API_KEY_2 = open('elevenLabs_key.txt', 'r').read()
elevenlabs.set_api_key(API_KEY_2)

# Initialize chapter_str as an empty string
chapter_str = ""


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST', 'GET'])
def generate_story():
    global chapter_str
    user_question = ""
    story = None
    if request.method == 'POST':
        if 'search_btn' in request.form:

            user_question = request.form.get('text-field')
            age = request.form.get('age-field')
            chapter = request.form.get('chapter-field')
            language = request.form.get('language-field')

            language_field = "Generate it to " + language + " language."
            user_result = (
                    "Create a dictionary.where key=1,value=string.string values is chapter. This are " + chapter +
                    " chapters heading for " + user_question + "." )
            test_model_01 = openai.chat.completions.create(
                                                model="gpt-3.5-turbo",
                                                messages=[{"role": "user",
                                                        "content": user_result}]
                                                                            )
            result_of_title = test_model_01.choices[0].message.content
            print(result_of_title)
            try:
                dictionary = eval(result_of_title)
                if isinstance(dictionary, dict):
                    chapter_explanations = []
                    print(chapter_explanations)
                    for i in range(1, len(dictionary) + 1):
                        per_chapter = dictionary[i]
                        chapter_explanations.append(f"chapter-{i}-{per_chapter} \n")
                        language_field_2 = "Write it to " + language + " language"
                        result = per_chapter + " explain it in " + EXPECTATION_WORDS + " words. " + language_field_2
                        print(result)
                        test_model_02 = openai.chat.completions.create(
                            model="gpt-4",
                            messages=[{"role": "user", "content": result}]
                        )
                        gpt_result = test_model_02.choices[0].message.content
                        print(gpt_result)
                        chapter_explanations.append(f"{gpt_result}\n\n\n")
                    chapter_str = "\n".join(chapter_explanations)

                    return render_template('generate.html', result=chapter_str,
                                           user_question=user_question, age=age, language=language)
                else:
                    print("The string does not represent a valid dictionary.")
                    print("Search Again.")
            except Exception as e:
                print("An error occurred while converting the string to a dictionary:", e)
                print("Restart Your Program.")

        elif 'save_btn' in request.form:
            if chapter_str:
                input_story_name = request.form.get('input-story-name')
                age = request.form.get('user-age')
                language = request.form.get('select-language')

                folder_name = 'Collection'
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                file_path = os.path.join(folder_name, f'{input_story_name}_story.txt')
                with open(file_path, 'w') as file:
                    file.write(chapter_str)

                story = Story(story_name=input_story_name, file=f'{input_story_name}_story', content=chapter_str,
                              age=age, language=language)
                db.session.add(story)
                db.session.commit()

                # send_file(file_path, as_attachment=True)
                return render_template('voiceTest_and_download.html', story=story)
            else:
                return 'Content not available'
    return render_template('index.html')


@app.route('/view_list', methods=['GET'])
def view_list():
    stories = Story.query.all()
    return render_template('view_list.html', stories=stories)


# @app.route('/view_file/<int:story_id>', methods=['GET'])
# def view_file(story_id):
#     session = db.session
#     story = session.get(Story, story_id)
#     if story:
#         return render_template('view_file.html', story=story)
#     return "Story not found."

@app.route('/view_test_file/<int:story_id>', methods=['GET'])
def view_test_file(story_id):
    session = db.session
    story = session.get(Story, story_id)
    if story:
        file_path = os.path.join("Mp3" , f"{story.story_name}_{story.id}.mp3")
        if os.path.exists(file_path):
            return render_template('read_content_file.html', story=story)
        else:
            return render_template('voiceTest_and_download.html', story=story)
    return "Story not found."


@app.route('/delete_file/<int:story_id>', methods=['GET', 'POST'])
def delete_file(story_id):
    """
        This is delete methods.
    """
    if request.method == 'POST':
        file_delete = Story.query.get_or_404(story_id)

        try:
            db.session.delete(file_delete)
            db.session.commit()
            return redirect('/view_list')
        except:
            return "There was a problem deleting the data."

    # Handle GET requests for displaying the form or other actions here
    return "GET request for deleting a file"


@app.route('/update_file/<int:story_id>', methods=['POST','GET'])
def update_file(story_id):
    """
        This is update route.
    """
    session = db.session
    story = session.get(Story, story_id)
    if story:
        return render_template('update_file.html', story=story)
    return "Story not found"


@app.route('/update_story_name/<int:story_id>', methods=['GET', 'POST'])
def update_story_name(story_id):
    """Update story name."""
    stories = Story.query.all()
    session = db.session
    story = session.get(Story, story_id)
    if story:
        update_content = request.form.get('update-story-field')

        if update_content:
            story.story_name = update_content
            session.commit()
            return render_template('view_list.html', stories=stories)
        else:
            return "Update content cannot be empty"
    return "Invalid update request"


@app.route('/voiceTest_and_download/<int:story_id>', methods=['GET', 'POST'])
def voiceTest_and_download(story_id):
    """Check voice and download mp3 file."""
    global is_speaking  # Access the global variable
    is_speaking = False
    choice_voice = request.form.get('choice_voice')
    choice_model = request.form.get('choice_model')
    session = db.session
    story = session.get(Story, story_id)
    if story:
        
        if 'listen_voice' in request.form:
            audio = elevenlabs.generate(text=story.content[10:150],
                                        voice=choice_voice,
                                        model=choice_model)
            elevenlabs.play(audio)
            return render_template('voiceTest_and_download.html', story=story)

        elif 'download_mp3' in request.form:
            folder_name = "Mp3"
            absolute_folder_path = os.path.abspath(folder_name)

            if not os.path.exists(absolute_folder_path):
                os.makedirs(absolute_folder_path)

            audio = elevenlabs.generate(
                text=story.content,
                voice=choice_voice,
                model=choice_model
            )

            if not os.path.exists(f'{story.story_name}.mp3'):
                elevenlabs.save(audio, os.path.join(absolute_folder_path, f'{story.story_name}_{story.id}.mp3'))
                file_path = os.path.join(absolute_folder_path, f'{story.story_name}_{story.id}.mp3')
                send_file(file_path, as_attachment=True, mimetype='audio/mpeg')
                return render_template('read_content_file.html', story=story)
            else:
                print('This file already downloaded.')

        return "Invalid request method"
    else:
        return render_template('story_not_found.html')



@app.route('/view_file/<int:story_id>', methods=['GET', 'POST'])
def read_file(story_id):
    """read file content."""
    session = db.session
    story = session.get(Story, story_id)
    pygame.mixer.init()

    if story:
        if request.method == 'POST':
            pygame.mixer.music.load('Mp3/Soleman_8.mp3')
            if 'read_content' in request.form:
                pygame.mixer.music.play()
            elif 'pause_content' in request.form:
                pygame.mixer.music.pause()
            elif 'resume_content' in request.form:
                pygame.mixer.music.unpause()
            elif 'stop_content' in request.form:
                pygame.mixer.music.stop()

        return render_template('read_content_file.html', story=story)
    else:
        return render_template('story_not_found.html')


# Error handling section.
@app.errorhandler(404)
def not_found(e):
    """Its handel 404 error"""
    print(e)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Its handel 500 error message."""
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
