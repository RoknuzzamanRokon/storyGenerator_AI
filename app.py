from flask import Flask, render_template, request, send_file, make_response,redirect,url_for
import openai
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import Session
# from mysql import connector
from datetime import datetime
import os
import pyttsx3


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/aistorywritter'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/storyGenText'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
session = Session()

engine = pyttsx3.init()
is_speaking = False


EXPECTATION_WORDS = '1000'


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_name = db.Column(db.String(255))
    file = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)

    def __repr__(self) -> str:
        return f'{self.id}-{self.story_name}'


API_KEY = open("secret_key.txt", "r").read()
openai.api_key = API_KEY

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
            langauge = request.form.get('language-field')

            langauge_field = "Generate it to " + langauge + " langauge."
            user_result = (
                    "Create a dictionary.where key=1,value=string.string values is chapter. This are " + chapter +
                    " chapters heading for " + user_question + "." )
            test_model_01 = openai.chat.completions.create(model="gpt-3.5-turbo",
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
                        chapter_explanations.append(f"chapter-{i}>>>>>{per_chapter} \n")
                        langauge_field_2 = "Write it to " + langauge + " langauge"
                        result = per_chapter + " explain it in " + EXPECTATION_WORDS + " words. " + langauge_field_2
                        print(result)
                        test_model_02 = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": result}]
                        )
                        gpt_result = test_model_02.choices[0].message.content
                        print(gpt_result)
                        chapter_explanations.append(f"{gpt_result}\n\n\n")
                    chapter_str = "\n".join(chapter_explanations)

                    return render_template('generate.html', result=chapter_str, user_question=user_question)
                else:
                    print("The string does not represent a valid dictionary.")
                    print("Search Again.")
            except Exception as e:
                print("An error occurred while converting the string to a dictionary:", e)
                print("Restart Your Program.")

        elif 'save_btn' in request.form:
            if chapter_str:

                input_story_name = request.form.get('input-story-name')
                folder_name = 'Collection'
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                file_path = os.path.join(folder_name, f'{input_story_name} story.txt')
                with open(file_path, 'w') as file:
                    file.write(chapter_str)

                story = Story(story_name=input_story_name, file=f'{input_story_name} story', content=chapter_str)
                db.session.add(story)
                db.session.commit()

                # send_file(file_path, as_attachment=True)
                return render_template('generate.html', result=chapter_str)
            else:
                return 'Content not available'
    return render_template('index.html')


@app.route('/view_list', methods=['GET'])
def view_list():
    stories = Story.query.all()
    return render_template('view_list.html', stories=stories)


@app.route('/view_file/<int:story_id>', methods=['GET'])
def view_file(story_id):
    session = db.session
    story = session.get(Story, story_id)
    if story:
        return render_template('view_file.html', story=story)
    return "Story not found."


@app.route('/delete_file/<int:story_id>', methods=['GET', 'POST'])
def delete_file(story_id):
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
    session = db.session
    story = session.get(Story, story_id)
    if story:
        return render_template('update_file.html', story=story)
    return "Story not found"


@app.route('/update_story_name/<int:story_id>', methods=['GET', 'POST'])
def update_story_name(story_id):
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






@app.route('/view_file/<int:story_id>', methods=['GET', 'POST'])
def view_or_read_file(story_id):
    global is_speaking  # Access the global variable
    is_speaking = False
    session = db.session
    story = session.get(Story, story_id)
    if story:
        if request.method == 'POST':
            if 'read_file' in request.form:
                # Start text-to-speech
                if not is_speaking:
                    engine.say(story.content)
                    engine.runAndWait()
                    is_speaking = True
            elif 'stop_content' in request.form:
                # Stop text-to-speech
                if is_speaking:
                    engine.stop()
                    is_speaking = False
        return render_template('view_file.html', story=story)
    else:
        return render_template('story_not_found.html')





# @app.route('/view_file/<int:story_id>', methods=['GET', 'POST'])
# def view_or_read_file(story_id):
#     story = Story.query.get(story_id)
#     if story:
#         if request.method == 'POST':
#             engine = pyttsx3.init()
#             engine.say(story.content)
#             engine.runAndWait()
#             return redirect(url_for('view_or_read_file', story_id=story_id))
#         return render_template('view_file.html', story=story)
#     else:
#         return render_template('story_not_found.html')


#
# @app.route('/update_list/<int:story_id>', methods=['GET', 'POST'])
# def update_story(story_id):
#     story = Story.query.get(story_id)
#     if story:
#         if request.method == 'POST':
#             new_content = request.form.get('new_content')
#             if new_content:
#                 story.content = new_content
#                 db.session.commit()
#
#             else:
#                 return "Its Empty"
#         return render_template('update_story.html', story=story)
#     return "Story not found"
#
#
#

if __name__ == "__main__":
    app.run(debug=True)
