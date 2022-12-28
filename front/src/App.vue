<template>
  <div class="common-layout">
    <el-container class="layout-container" style="height: 700px">
      <el-container>
        <el-aside width="20%">
          <el-menu default-active="0"  @open="handleOpen" @close="handleClose"
            @select="handleSelect">
            <el-menu-item index="HelloWorld">
              <span>首页</span>
            </el-menu-item>
            <el-menu-item index="ID">
              <span>身份识别</span>
            </el-menu-item>
            <el-menu-item index="404" disabled>
              <span>群体计数</span>
            </el-menu-item>
            <el-menu-item index="404" disabled>
              <span>表型估计</span>
            </el-menu-item>
            <el-menu-item index="Explain">
              <span>说明</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <!-- 路由出口-->
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from "vue-router";
const router = useRouter();
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
  router.push({
    name: key,
    params: {
      msg: keyPath
    }
  });
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #67C23A;
}

</style>
