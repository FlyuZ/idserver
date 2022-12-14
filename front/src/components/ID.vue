<template>
  <el-steps
    :active="active"
    finish-status="success"
    simple
    style="margin-top: 20px"
  >
    <el-step title="更新检索库" />
    <el-step title="上传数据" />
    <el-step title="开始识别" />
  </el-steps>
  
</template>



<script setup>
import {reactive, onMounted } from "vue";
const data = reactive({ active: 0 })
// updateGallery(      async () => {
//         const rsp1 = await fetch(`http://127.0.0.1:8010/hello`).then((rsp) =>
//           rsp.text()
//         );
//         data.text1 = rsp1;
//         const rsp2 = await fetch(`http://127.0.0.1:8010/hello`, {
//           method: "POST",
//         }).then((rsp) => rsp.text());
//         data.text2 = rsp2;
//       });
</script>