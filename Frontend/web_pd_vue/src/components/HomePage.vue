<template>
  <div class="container-fluid">
    <h1 class="mb-4">{{ msg }}</h1>

    <div class="btn-group-vertical">
      <button class="btn btn-primary mb-2" @click="makeGetSingleRequest">Make GET Single Request</button>
      <button class="btn btn-success mb-2" @click="makeGetCollectionRequest">Make GET Collection Request</button>
      <button class="btn btn-info mb-2" @click="makePostRequest">Make POST Request</button>
      <button class="btn btn-danger mb-2" @click="makeDeleteRequest">Make Delete Request</button>
    </div>

    <div class="row md-4">
      <label for="postId">Enter Post ID:</label>
      <input type="text" class="form-control" id="postId" v-model="postId" />
      <label for="bpm" class="mt-2">BPM:</label>
      <input type="number" class="form-control" id="bpm" v-model="postData.bpm" />
      <label for="postId">Enter Title:</label>
      <input type="text" class="form-control" id="name" v-model="postData.name" />
      <h2 class="mt-2">{{ content }}</h2>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      content:null,
      url: "http://localhost:8080/api/v1.0/audios",
      postData: {
        name: "", // Input for title
        bpm: "", // Input for description
      },
    };
  },
  name: "HomePage",
  props: {
    msg: String,
  },
  methods: {
    makeGetCollectionRequest() {
      axios.get(this.url).then((res) => (this.content = res.data));
    },
    makeGetSingleRequest() {
      console.log("Making GET request to:", `${this.url}/${this.postId}`);
      axios
        .get(`${this.url}/${this.postId}`)
        .then((res) => {
          console.log("Response:", res.data);
          this.content = res.data;
        })
        .catch((error) => {
          console.error("Error making GET single request:", error);
        });
    },
    makePostRequest() {
      console.log("Making POST request to:", this.url);
      axios
        .post(this.url, this.postData)
        .then((res) => {
          console.log("Response:", res.data);
          this.content = res.data;
        })
        .catch((error) => {
          console.error("Error making POST request:", error);
        });
    },
    makeDeleteRequest() {
      console.log("Making DELETE request to:", `${this.url}/${this.postId}`);
      axios
        .delete(`${this.url}/${this.postId}`)
        .then((res) => {
          console.log("Response:", res.data);
          this.content = res.data;
        })
        .catch((error) => {
          console.error("Error making GET single request:", error);
        });
    },
  },
};
</script>

<style scoped>
/* Add scoped styles if needed */
</style>
