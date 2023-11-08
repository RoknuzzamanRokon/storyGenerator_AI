<template>
  <div>
    <!-- Add your Vue components for UI elements here -->
    <input v-model="chapter" placeholder="Chapter" />
    <input v-model="user_question" placeholder="User Question" />
    <button @click="search">Search</button>
    <button @click="save">Save</button>
    <div>{{ result }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      chapter: '',
      user_question: '',
      result: '',
    };
  },
  methods: {
    search() {
      axios.post('http://127.0.0.1:5000/get_user_input', {
        chapter: this.chapter,
        user_question: this.user_question,
        dropdown_value_language: this.dropdown_value_language,
      })
      .then(response => {
        this.result = response.data.result;
      })
      .catch(error => {
        console.error(error);
      });
    },
    save() {
      // Add logic to save the result to a file if needed
    },
  },
};
</script>
