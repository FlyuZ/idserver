<template>
  <div class="common-layout" style="height: 100%">
    <el-container>
      <el-header class="title">
        <el-row>
          <el-col :span="4"
            ><img
              style="height: 60px"
              alt="nwafu logo"
              src="../assets/nwafu.png"
          /></el-col>
          <el-col :span="14">羊只个体身份管理系统</el-col>
          <el-col :span="6"
            ><img
              style="height: 60px"
              alt="sheep logo"
              src="../assets/icon-sheep.png"
          /></el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-aside width="50%" style="padding: 10px">
          <el-card shadow="always" style="height: 400px">
            <el-row>
              <el-col :span="24" :gutter="20" style="margin-bottom: 20px">
                <el-table
                  :data="GalleryInfo"
                  style="width: 100%; height: 300px"
                  stripe
                >
                  <el-table-column prop="gallery" label="Gallery" />
                  <el-table-column prop="name" label="Name" />
                  <el-table-column label="Operations">
                    <template #default="scope">
                      <el-button
                        link
                        type="primary"
                        size="small"
                        @click="Detail(scope.$index, scope.row)"
                        >查看详情</el-button
                      >
                    </template>
                  </el-table-column>
                </el-table>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="12" :gutter="20" style="margin-bottom: 20px">
                <el-button
                  type="primary"
                  @click="register"
                  style="width: 150px; font-size: 16px; letter-spacing: 5px"
                  >新增注册</el-button
                >
              </el-col>
              <el-col :span="12">
                <el-button
                  type="primary"
                  @click="updateGallery"
                  style="width: 150px; font-size: 16px; letter-spacing: 5px"
                  >更新检索库</el-button
                >
              </el-col>
            </el-row>
          </el-card>
        </el-aside>
        <el-main width="50%" style="padding: 10px">
          <el-card shadow="always" style="height: 400px">
            <el-table :data="IDInfo" style="width: 100%; height: 360px" stripe>
              <el-table-column prop="gallery" label="Gallery" />
              <el-table-column prop="id" label="ID" />
              <el-table-column prop="info" label="Info" />
              <el-table-column label="Operations">
                <template #default="scope">
                  <el-button
                    link
                    type="primary"
                    size="small"
                    @click="Edit(scope.$index, scope.row)"
                    >编辑</el-button
                  >
                  <!-- <el-button link type="primary" size="small"
                                        @click="Delete(scope.$index, scope.row)">删除</el-button> -->
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script lang="ts" setup>
import { ElLoading, ElMessage, ElMessageBox } from "element-plus";
import { defineComponent, ref } from "vue";
import axios from "axios";

interface ID {
  gallery: string;
  id: string;
  info: string;
}
interface Gallery {
  gallery: string;
  name: string;
}
let IDInfo = ref<ID[]>([
  {
    gallery: "test",
    id: "test",
    info: "test",
  },
]);
let GalleryInfo = ref<Gallery[]>([
  {
    gallery: "test",
    name: "test",
  },
]);

const Detail = (index: number, row: Gallery) => {
  console.log("click");
};
const Delete = (index: number, row: ID) => {
  console.log("click");
};
const Edit = (index: number, row: ID) => {
  console.log("click");
};

const register = () => {
  console.log("click");
  ElMessageBox.confirm("新身份将会被注册", "提示", {
    confirmButtonText: "确认",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(() => {
      axios
        .get("/api/updategalleryinfo")
        .then((res) => {
          IDInfo.value = res.data[0];
          GalleryInfo.value = res.data[1];
          console.log(IDInfo.value);
        })
        .catch((err) => {
          console.log(err);
        });
      ElMessage({
        type: "success",
        message: "注册成功",
      });
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "注册失败",
      });
    });
};

const updateGallery = () => {
  console.log("click");
  const loading = ElLoading.service({
    lock: true,
    text: "Loading",
    background: "rgba(0, 0, 0, 0.7)",
  });
  axios
    .get("/api/updategalleryfeats")
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });

  setTimeout(() => {
    loading.close();
    ElMessage({
      showClose: true,
      message: "更新成功.",
      type: "success",
    });
  }, 5000);
};
</script>

<style>
.title {
  font-size: 40px;
  font-weight: bold;
  color: #21b3b9;
  align-items: center;
  justify-content: center;
  letter-spacing: 20px;
}
</style>