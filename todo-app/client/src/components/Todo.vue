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
      <button @click="postTodo()">POST DATA</button>

      <hr />
      <input v-model="id" />
      <button @click="fetchTodo()">GET BY ID</button>
      <button @click="deleteTodo()">DELETE BY ID</button>
      <button @click="updateTodo()">UPDATE BY ID</button>
      <pre>{{ getTodo }}</pre>
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
      todo: null,
      title: "",
      task: "",
      id: ""
    };
  },
  methods: {
    async fetchTodos() {
      try {
        const data = await getData(`${baseUrl}todo/`);
        this.todos = [...data];
      } catch (error) {
        console.error(error);
      }
    },
    async fetchTodo() {
      try {
        const data = await getData(`${baseUrl}todo/${this.id}`);
        this.todo = { ...data };
        this.id = "";
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
        await this.fetchTodos();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteTodo() {
      try {
        const response = await postData(
          `${baseUrl}todo/${this.id}`,
          {},
          "DELETE"
        );
        this.id = "";
        this.todo = null;
        await this.fetchTodos();
      } catch (error) {
        console.error(error);
      }
    },
    async updateTodo() {
      try {
        const response = await postData(
          `${baseUrl}todo/${this.id}`,
          {
            title: this.title,
            task: this.task
          },
          "PUT"
        );
        this.id = "";
        await this.fetchTodos();
      } catch (error) {
        console.error(error);
      }
    }
  },
  computed: {
    getTodos() {
      return this.todos;
    },
    getTodo() {
      return this.todo;
    }
  }
};
</script>
