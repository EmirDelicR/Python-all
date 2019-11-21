<template>
  <div class="hello">
    <div>
      <h3>Create User</h3>
      <button @click="createUser()">CREATE USER</button>
    </div>
  </div>
</template>

<script>
import { postData, getData } from "@/utils/api";
import { baseUrl } from "@/utils/constants";
export default {
  name: "User",
  data() {
    return {
      selected: ""
    };
  },
  methods: {
    async testGetMethod() {
      const response = await postData(`${baseUrl}login/`, {
        username: "Test User",
        password: "Test123"
      });
    }
  },
  computed: {}
};
</script>
