<template>
  <div class="hello">
    <div>
      <h3>Get Todo</h3>
      <div style="border:1px solid red" v-if="isError">{{ msg }}</div>
      <div style="border:1px solid green" v-if="isSuccess">{{ msg }}</div>
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
      id: "",
      msg: "",
      isError: false,
      isSuccess: false
    };
  },
  methods: {
    updateResponseStatus(response) {
      this.isError = response.error;
      this.isSuccess = !this.isError;

      if (this.isError || this.isSuccess) {
        this.msg = response.message;
      }
    },

    async fetchTodos() {
      try {
        const response = await getData(`${baseUrl}todo/`, true);
        this.todos = [...response];
      } catch (error) {
        console.error(error);
      }
    },
    async fetchTodo() {
      try {
        const response = await getData(`${baseUrl}todo/${this.id}`);
        this.isError = response.error;

        if (this.isError) {
          this.msg = response.message;
          return;
        }
        this.todo = { ...response.data };
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

        await this.updateResponseStatus(response);

        if (this.isError) {
          return;
        }

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

        await this.updateResponseStatus(response);

        if (this.isError) {
          return;
        }

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

        await this.updateResponseStatus(response);

        if (this.isError) {
          return;
        }

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
