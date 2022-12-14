<template>
  <el-row class="tac">
    <el-col :span="4">
      <h5 class="mb-2">功能菜单</h5>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>身份识别</span>
          </template>
            <el-menu-item index="1-1">选择Gallery库</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
            <el-menu-item index="1-3">item three</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="2" disabled>
          <el-icon><icon-menu /></el-icon>
          <span>群体计数</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>表型估计</span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <h5 class="mb-2">Custom colors</h5>
      <img alt="Vue logo" src="./assets/logo.png" />
      <HelloWorld msg="Welcome to Your Vue.js + Vite App" />
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
import HelloWorld from "./components/HelloWorld.vue";
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from "@element-plus/icons-vue";
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
