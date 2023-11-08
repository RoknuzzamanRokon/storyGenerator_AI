<template>
    <div>
      <!-- <button @click="showModal">Show Modal</button> -->
      <div class="modal fade" :class="{ 'show': modalVisible }" tabindex="-1" aria-labelledby="sticky-modal" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Sticky Modal</h5>
              <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <!-- Your content here -->
              <div v-if="activePanel === 1">
                <h4>Panel 1 Content</h4>
                <button @click="showNextPanel">Next Panel</button>
              </div>
              <div v-else-if="activePanel === 2">
                <h4>Panel 2 Content</h4>
                <button @click="showNextPanel">Next Panel</button>
              </div>
              <div v-else>
                <h4>Panel 3 Content</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        modalVisible: false,
        activePanel: 1,
      };
    },
    methods: {
      showModal() {
        this.modalVisible = true;
        this.activePanel = 1; 
      },
      closeModal() {
        this.modalVisible = false;
      },
      showNextPanel() {
        this.activePanel++;
      },
    },
  };
  </script>
  