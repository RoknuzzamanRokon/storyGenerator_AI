<template>
  <div>
    <section class="main-banner-style06 full-screen p-0 header-position">
      <div class="stratup-image">
        <img
          src="https://wallpapers.com/images/hd/corner-building-for-4k-white-background-tsx7c82luhg36ygy.jpg"
          alt="..."
        />
      </div>

      <div class="container lg-container d-flex flex-column">
        <div class="row align-items-center min-vh-100">
          <div class="col-lg-7 z-index-2">
            <form @submit.prevent="generateStory">
              <div class="card">
                <div class="card-body">
                  <div class="row">
                    <label for="" class="form-label"
                      >Select Story Category <span>*</span></label
                    >
                    <div class="col-md-4">
                      <div class="card">
                        <div class="card-body">
                          <input
                            type="radio"
                            v-model="selectedGenre"
                            value="Fiction"
                          />
                          Fiction
                        </div>
                      </div>
                    </div>
                    <div class="col-md-4">
                      <div class="card">
                        <div class="card-body">
                          <input
                            type="radio"
                            v-model="selectedGenre"
                            value="Non-Fiction"
                          />
                          Non-Fiction
                        </div>
                      </div>
                    </div>
                    <div class="col-md-4">
                      <div class="card">
                        <div class="card-body">
                          <input
                            type="radio"
                            v-model="selectedGenre"
                            value="Educational"
                          />
                          Educational
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="row">
                    <div class="container">
                      <div class="py-2">
                        <label for="" class="form-label"
                          >Enter topic or Pickup line</label
                        >
                        <textarea
                          class="form-control"
                          cols="15"
                          rows="5"
                          v-model="storyLine"
                          placeholder="Enter topic or Pickup line"
                        ></textarea>
                      </div>
                    </div>
                    <div class="col-md-3">
                      <button
                        style="float: left"
                        @click="generateSurprise"
                        class="btn btn-outline-success"
                      >
                        Surprise Me!
                      </button>
                    </div>
                  </div>

                  <div class="row py-3">
                    <div class="col-md-4">
                      <div class="mb-3">
                        <select v-model="selectedLanguage" class="form-control">
                          <option selected>Select Language *</option>
                          <option value="German">German</option>
                          <option value="English">English</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-4">
                      <div class="mb-3">
                        <select v-model="selectedStyle" class="form-control">
                          <option selected>Select Genre *</option>
                          <option value="LUL">LUL</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-4">
                      <select v-model="readerAge" class="form-control">
                        <option selected>Select Reader Age *</option>
                        <option value="1">1 - 5</option>
                        <option value="6">6 - 10</option>
                        <option value="11">11 - 15</option>
                        <option value="16">16 - 18</option>
                        <option value="18">18 - 65</option>
                      </select>
                    </div>
                    <div class="col-md-4">
                      <div class="d-grid gap-2">
                        <button
                          class="btn btn-outline-success btn-lg"
                          type="submit"
                        >
                          Generate Story
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <div class="container">
  <h2>Generated Story</h2>
  <div v-if="selectedLanguage === 'English'">
    {{ generatedStory }}
  </div>
  <div v-else-if="selectedLanguage === 'German'">
    {{ translateToGerman(generatedStory) }}
  </div>
</div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      selectedGenre: "",
      storyLine: "",
      selectedLanguage: "English",
      selectedStyle: "",
      readerAge: "",
      chapterCount: 5,
      generatedStory: "",
    };
  },
  methods: {
    generateSurprise() {
      // Generate a 110-word story and update the storyLine
      // Assuming you have a function to generate a story
      this.storyLine = this.generateRandomStory();
    },
    generateStory() {
      const requestData = {
        genre: this.selectedGenre,
        storyLine: this.storyLine,
        language: this.selectedLanguage,
        style: this.selectedStyle,
        readerAge: this.readerAge,
        chapterCount: this.chapterCount,
      };

      // Use Axios to send the POST request
      axios
        .post("http://127.0.0.1:5000/generateStory", requestData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.generatedStory = response.data.generatedStory;
        })
        .catch((error) => {
          console.error("Error generating story:", error);
        });
    },
    // Generate a random 110-word story
    generateRandomStory() {
      // Replace this with your story generation logic
      // Here's an example that generates a random story
      const words = [
        "Once", "upon", "a", "time,", "in", "a", "land", "far", "far", "away,",
        "there", "lived", "a", "brave", "knight", "named", "Sir", "Lancelot.",
        // ... continue with more words ...
      ];

      let story = "";
      for (let i = 0; i < 110; i++) {
        const randomIndex = Math.floor(Math.random() * words.length);
        story += words[randomIndex] + " ";
      }

      return story;
    },
  },
};
</script>