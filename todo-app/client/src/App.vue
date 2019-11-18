<template>
  <div id="app">
    <Todo />
    <hr />
    <test-api-view />
  </div>
</template>

<script>
import Todo from "./components/Todo.vue";
import TestApiView from "./components/TestApiView";

export default {
  name: "app",
  components: {
    Todo,
    TestApiView
  }
};
</script>

<style></style>
