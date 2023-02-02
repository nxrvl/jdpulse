<template>
  <div>
    <form @submit.prevent="submitHandler" >
      <div class="form-group">
        <textarea class="form-control" aria-label="With textarea" v-model="inputValue"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div>
      <ul>
        <li v-for="(item, index) in apiResponse" :key="index">{{ index + 1 }}. {{ item }}</li>
      </ul>
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
      apiResponse: []
    }
  },
  methods: {
    async submitHandler() {
      try {
        const response = await axios.get('http://localhost:8000/extract', { params: {text: this.inputValue} })
        this.apiResponse = response.data
      } catch (error) {
        console.error(error)
      }
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
</style>