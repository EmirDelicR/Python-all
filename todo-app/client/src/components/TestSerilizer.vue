<template>
  <div class="hello">
    <div>
      <h3>Test Serilizer</h3>
      <button @click="testSerilizer()">TEST</button>
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
    testSerilizer() {
      console.log("Test");
    }
  },
  computed: {}
};
</script>
