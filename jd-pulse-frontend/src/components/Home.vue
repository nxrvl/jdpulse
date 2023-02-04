<template>
  <div>
    <!-- Modal -->
    <div class="modal" tabindex="-1" role="dialog" v-if="showErrorModal">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Error</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="showErrorModal = false">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>{{ errorMessage }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="showErrorModal = false">Close</button>
          </div>
        </div>
      </div>
    </div>
    <form @submit.prevent="submitHandler" >
      <div class="form-group">
        <textarea class="form-control" aria-label="With textarea" v-model="inputValue"></textarea>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="loading">
        <span v-if="loading">Loading...</span>
        <span v-else>Submit</span>
      </button>
    </form>
    <div class="d-flex flex-wrap" style="margin: 5% 10% 0% 10%">
      <div v-if="!showErrorModal" class="d-flex flex-wrap" style="margin: 5% 10% 0% 10%">
        <div class="badge badge-pill m-1"
             v-for="(item, index) in apiResponse"
             :key="index"
             :class="{ copied: item === copiedItem }"
             @click="copyToClipboard(item)">
          {{ item }}
        </div>
      </div>

    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: "Home",
  data() {
    return {
      inputValue: '',
      apiResponse: ["test"],
      loading: false,
      copiedItem: null,
      showErrorModal: false,
      errorMessage: ''
    }
  },
  methods: {
    async submitHandler() {
      this.loading = true;
      try {
        const response = await axios.get('http://localhost:8000/api/extract', {params: {text: this.inputValue}})
        if (response.data.error) {
          console.log(response.data.error)
          this.errorMessage = response.data.error;
          this.showErrorModal = true;
        } else {
          this.apiResponse = response.data
          this.loading = false;
        }
      } catch
          (error) {
        console.error(error)
      }
    },

    async copyToClipboard(item) {
      // Copy the item to the clipboard
      await navigator.clipboard.writeText(item).then(() => {
        // Update the copied item in the data
        this.copiedItem = item;
        // Reset the copied item after 1 second
        setTimeout(() => {
          this.copiedItem = null;
        }, 200);
      });
    }
  }
}
</script>

<style scoped>
.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  margin-top: 10px;
}
.badge {
  font-size: 16px;
  background-color: #007bff;
  padding: 5px 10px;
  border-radius: 5px;
}
.badge.copied {
  background-color: cornflowerblue;
  color: white;
  #transition: background-color 1s ease;
}
</style>

