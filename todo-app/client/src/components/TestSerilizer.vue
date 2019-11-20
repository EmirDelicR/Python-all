<template>
  <div class="hello">
    <div>
      <h3>Test Serilizer</h3>
      <button @click="testGetMethod()">GET</button>
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
    testGetMethod() {
      console.log("Test");
    }
  },
  computed: {}
};
</script>
