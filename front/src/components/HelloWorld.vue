<template>
  <div>
    <img alt="Vue logo" src="../assets/logo.png" />
    <h1>{{ msg }}</h1>

    <p>
      <a href="https://vitejs.dev/guide/features.html" target="_blank">
        Vite Documentation
      </a>
      |
      <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
    </p>
  </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";

defineProps({
  msg: String,
});

const state = reactive({ count: 0 });
const data = reactive({ text1: "" });

onMounted(async () => {
  const rsp1 = await fetch(`http://127.0.0.1:8010/hello`).then((rsp) =>
    rsp.text()
  );
  data.text1 = rsp1;
  const rsp2 = await fetch(`http://127.0.0.1:8010/hello`, {
    method: "POST",
  }).then((rsp) => rsp.text());
  data.text2 = rsp2;
});
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
