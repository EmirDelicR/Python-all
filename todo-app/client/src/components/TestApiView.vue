<template>
  <div class="hello">
    <div>
      <h3>Test APIView</h3>

      <h5>GET Method</h5>
      <p>Open console: press F12</p>
      <button @click="testGetMethod()">GET</button>
      <hr />
      <h3>Test ViewSet</h3>
      <button @click="testViewSetMethods()">TEST METHOD</button>
      <select v-model="selected">
        <option disabled value>Please select one</option>
        <option>GET</option>
        <option>GET BY ID</option>
        <option>POST</option>
        <option>PUT</option>
        <option>PATCH</option>
        <option>DELETE</option>
      </select>
      <br />
      <button @click="callCustomAction()">CUSTOM ACTION</button>
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
      selected: ""
    };
  },
  methods: {
    /** Helper method to execute GET function (ViewMethodSet) */
    async executeGet(methodConfig) {
      let response = await getData(`${baseUrl}test-model-view-set/`, true);
      console.log("GET response: ", response);
      if (methodConfig.byId) {
        const ID = response[0] ? response[0].id : null;
        if (ID === null) {
          console.log("First Create TODO!!");
          return;
        }
        response = await getData(`${baseUrl}test-model-view-set/?pk=${ID}`);
        console.log("GET BY ID response: ", response);
        return response;
      }
    },
    /** Helper function to execute POST function (ViewMethodSet) */
    async executePost(methodConfig) {
      if (methodConfig.byId) {
        const todoItem = await this.executeGet(methodConfig);

        const response = await postData(
          `${baseUrl}test-model-view-set/${todoItem.id}/`,
          {
            title: "Test UPDATE/PATCH Title",
            task: "Test UPDATE/PATCH Task"
          },
          `${methodConfig.name}`
        );
        console.log("Response: ", response);
        return;
      }

      const response = await postData(
        `${baseUrl}test-model-view-set/`,
        {
          title: "Test Post Title",
          task: "Test Post Task"
        },
        `${methodConfig.name}`
      );
      console.log("POST METHOD response: ", response);
    },
    /** Normal get function for ApiView */
    async testGetMethod() {
      try {
        const response = await getData(`${baseUrl}test-api-view/`);
        console.log(response);
        return response;
      } catch (error) {
        console.error(error);
      }
    },
    /** Method to execute all others methods like POST,GET ... */
    async testViewSetMethods() {
      const methodConfig = await this.getMethodConfig;
      try {
        if (methodConfig.isGet) {
          await this.executeGet(methodConfig);
          return;
        } else {
          await this.executePost(methodConfig);
        }
      } catch (error) {
        console.error(error);
      }
    },
    /** Call custom methods in ViewModelSet */
    async callCustomAction() {
      try {
        const methodConfig = {
          byId: true
        };
        const todoItem = await this.executeGet(methodConfig);
        const response = await postData(
          `${baseUrl}test-model-view-set/set_todo/?pk=${todoItem.id}`,
          {
            title: "Test Post Title From Custom",
            task: "Test Post Task From Custom"
          }
        );
        console.log(response);
        return response;
      } catch (error) {
        console.error(error);
      }
    }
  },
  computed: {
    showGetResponse() {
      return this.todos;
    },
    getMethodConfig() {
      const selected = this.selected;
      let config = {
        name: "GET",
        byId: false,
        isGet: true
      };

      if (selected === "" || selected === "GET") {
        return config;
      }

      if (selected === "GET BY ID") {
        config.byId = true;
        return config;
      }

      config.name = selected;
      config.isGet = false;

      if (selected === "POST") {
        return config;
      }

      config.byId = true;

      return config;
    }
  }
};
</script>
