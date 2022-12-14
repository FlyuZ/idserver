<template>
<el-container>
   <el-aside width="15%">
      <h5 class="mb-2">功能菜单</h5>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        @select="handleSelect"
      >
        <el-sub-menu index="HelloWorld">
          <template #title>
            <el-icon><location /></el-icon>
            <span>身份识别</span>
          </template>
          <el-menu-item index="/index">选择Gallery库</el-menu-item>
          <el-menu-item index="/msg">item two</el-menu-item>
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
    </el-aside>
        <el-container>
            <el-header>欢 迎 使 用 </el-header>
            <el-main>
                <!-- 路由出口-->
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
  router.push(key)
}

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
