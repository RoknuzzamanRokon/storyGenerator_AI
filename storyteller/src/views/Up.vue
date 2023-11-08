<template>
  <div>
    <button @click="generateWords">Generate Words</button>
    <button @click="generateStory">Generate Story</button>
    <div>
      <h2>Generated Story</h2>
      <p v-if="generatedStory">{{ generatedStory }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      words: [], // Initialize an empty array to store generated words
      generatedStory: "", // Initialize an empty string for the generated story
    };
  },
  methods: {
    // Generate random words using a simple list (you can use a more extensive word list)
    generateWords() {
      const wordList = [
        "once", "upon", "a", "time", "in", "a", "land", "far", "away", "there",
        "lived", "a", "brave", "knight", "named", "Sir", "Lancelot",
        // Add more words to your list
      ];

      for (let i = 0; i < 5000; i++) {
        const randomIndex = Math.floor(Math.random() * wordList.length);
        const word = wordList[randomIndex];
        this.words.push(word);
      }
    },
    // Generate the story
    generateStory() {
      // Combine the generated words into a story
      this.generatedStory = this.words.join(" ");
    },
  },
};
</script>
