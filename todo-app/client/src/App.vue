<template>
  <div id="app">
    <user-login v-if="toShow" />
    <div v-else>
      <todo />
      <hr />
      <test-api-view />
      <hr />
      <test-serilizer />
    </div>
  </div>
</template>

<script>
import { getData } from "@/utils/api";
import { baseUrl } from "@/utils/constants";
import UserLogin from "./components/UserLogin";
import Todo from "./components/Todo.vue";
import TestApiView from "./components/TestApiView";
import TestSerilizer from "./components/TestSerilizer";

export default {
  name: "app",
  components: {
    UserLogin,
    Todo,
    TestApiView,
    TestSerilizer
  },
  data() {
    return {
      showLogin: true
    };
  },

  async beforeCreate() {
    const response = await getData(`${baseUrl}login/`);
    this.showLogin = response.error;
  },

  computed: {
    toShow() {
      return this.showLogin;
    }
  }
};
</script>
