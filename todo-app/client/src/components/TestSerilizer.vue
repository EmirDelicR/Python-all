<template>
  <div class="hello">
    <div>
      <h3>Test Serilizer</h3>
      <button @click="testGetSerilizer()">GET</button>
      <button @click="testPostSerilizer()">POST</button>
    </div>
  </div>
</template>

<script>
import { postData, getData } from "@/utils/api";
import { baseUrl } from "@/utils/constants";
export default {
  name: "Serilizer",
  data() {
    return {
      selected: ""
    };
  },
  methods: {
    async testGetSerilizer() {
      try {
        const response = await getData(`${baseUrl}test-serializer/`);
        console.log(response);
        return response;
      } catch (error) {
        console.error(error);
      }
    },
    async testPostSerilizer() {
      try {
        const response = await postData(`${baseUrl}test-serializer/`, {
          country: "Austria",
          city: "Linz",
          street: "Some Street",
          postal_code: "4040"
        });
        console.log(response);
        return response;
      } catch (error) {
        console.error(error);
      }
    }
  },
  computed: {}
};
</script>
