<template>
  <div id="app">
    <Todo />
    <hr />
    <test-api-view />
    <hr />
    <test-serilizer />
  </div>
</template>

<script>
import Todo from "./components/Todo.vue";
import TestApiView from "./components/TestApiView";
import TestSerilizer from "./components/TestSerilizer";

export default {
  name: "app",
  components: {
    Todo,
    TestApiView,
    TestSerilizer
  }
};
</script>
