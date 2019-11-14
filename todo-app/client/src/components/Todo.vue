<template>
  <div class="hello">
    <div>
      <h3>Get Todo</h3>
      <button @click="fetchTodos()">GET</button>
      <pre>{{ getTodos }}</pre>
      <hr />Title:
      <input v-model="title" />
      Task:
      <input v-model="task" />
      <button @click="postTodo()">Post Data</button>
    </div>
  </div>
</template>

<script>
import { postData, getData } from "@/utils/api";
import { baseUrl } from "@/utils/constants";
export default {
  name: "Todo",
  data() {
    return {
      todos: null,
      title: "",
      task: ""
    };
  },
  methods: {
    async fetchTodos() {
      try {
        const data = await getData(`${baseUrl}todo/`);
        this.todos = data;
      } catch (error) {
        console.error(error);
      }
    },
    async postTodo() {
      try {
        const response = await postData(`${baseUrl}todo/`, {
          title: this.title,
          task: this.task
        });
        console.log("tHIS IS AAA: ", response);
        if (response.status === 201) {
          console.log("Am i here");
          this.todos = await fetchTodos();
        }
      } catch (error) {
        console.error(error);
      }
    }
  },
  computed: {
    getTodos() {
      return this.todos;
    }
  }
};
</script>
