<template>
  <div class="common-layout" style="height:100%">
    <el-container>
      <el-header class="title">
        <el-row>
          <el-col :span="4"><img style="height:60px" alt="nwafu logo" src="../assets/nwafu.png" /></el-col>
          <el-col :span="14">羊只个体身份识别系统</el-col>
          <el-col :span="6"><img style="height:60px" alt="sheep logo" src="../assets/icon-sheep.png" /></el-col>
        </el-row>
      </el-header>

      <el-container>
        <el-aside width="35%" style="padding:10px;">
          <el-card class="left-card" shadow="always">
            <el-row :gutter="20" style="margin-bottom:50px;">
              <el-col :span="8" style="font-size:18px;">选择检索库</el-col>
              <el-col :span="16">
                <el-select v-model="galleryValue" placeholder="Select">
                  <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
              </el-col>
            </el-row>
            <el-row :gutter="20" style="margin-bottom:50px;">
              <el-col :span="8" style="font-size:18px;">选择数据源</el-col>
              <el-col :span="16">
                <el-radio-group v-model="radio1" @change="changeDataSrc">
                  <el-radio-button label="视频流" />
                  <el-radio-button label="图 像" selected />
                </el-radio-group>
              </el-col>
            </el-row>
            <el-row style="margin-bottom:50px;">
              <el-col :span="24">
                <el-button type="primary" @click="initIDenv"
                  style="width:150px;font-size:16px;letter-spacing:5px;">开始加载</el-button>
              </el-col>
            </el-row>
          </el-card>
        </el-aside>

        <el-main width="65%" style="padding:10px">
          <el-card class="right-card" shadow="always">
            <div class="imageid" :class="{ displayType: !type }">
              <el-row justify="center" style="margin-bottom:20px;width:200px">
                <el-col :span="24">
                  <el-upload :class="{ disUoloadBtn: noneBtnImg }" action="#" list-type="picture-card" accept="image/*"
                    :limit="1" :auto-upload="false" :on-remove="handleRemove" :on-change="handleChange">
                    <el-icon :size="50"><upload-filled /></el-icon>
                  </el-upload>
                </el-col>
              </el-row>
              <el-row justify="center" style="margin-bottom:30px;font-size:18px; ">
                <el-col :span="16" v-model="imgidtext">
                  {{ imgidtext }}
                </el-col>
              </el-row>
              <el-row justify="center" style="margin-bottom:20px;">
                <el-col :span="24">
                  <el-button type="primary" @click="startimage"
                    style="width:150px;font-size:16px;letter-spacing:5px;">开始识别</el-button>
                </el-col>
              </el-row>
            </div>

            <div class="videoid" :class="{ displayType: type }">
              <el-row justify="center" style="margin-bottom:10px;">
                <el-col :span="12">
                  <el-skeleton style="width: 250px" :loading="loading" animated>
                    <template #default>
                      <el-skeleton-item variant="image" style="width: 250px; height: 250px" />
                    </template>
                    <template #template>
                      <el-card :body-style="{ padding: '0px', marginBottom: '0px' }">
                        <img style="width:250px;  height:250px" :src="imgurl" />
                      </el-card>
                    </template>
                  </el-skeleton>
                </el-col>
                <el-col :span="12">
                  <el-table :data="videoData" height="250" style="width:450px;">
                    <el-table-column type="index"/>
                    <el-table-column prop="data" label="Data" />
                    <el-table-column prop="gallery" label="Gallery" />
                    <el-table-column prop="id" label="ID" />
                  </el-table>
                </el-col>
              </el-row>

              <el-row justify="center" style="margin-bottom:20px;font-size:18px; ">
                <el-col :span="20" v-model="videoidtext">
                  {{ videoidtext }}
                </el-col>
              </el-row>

              <el-row justify="center" style="margin-bottom:20px">
                <el-col :span="16">
                  <el-input v-model="inputIP" placeholder="请输入IP地址，开始识别" clearable />
                </el-col>
                <el-col :span="8">
                  <el-switch v-model="loading" @change="swithchange"  inline-prompt  size="large"
                  active-text="开始"
                  inactive-text="暂停"
                  />
                </el-col>
              </el-row>
            </div>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </div>

</template>



<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from 'element-plus'
import type { TableColumnCtx } from 'element-plus'
import { Plus, UploadFilled } from '@element-plus/icons-vue'
import axios from "axios"

const active = ref(0)
const galleryValue = ref('')
const radio1 = ref('图 像')
const noneBtnImg = ref(false)
const curfile = ref(null)
const imgidtext = ref('')
const videoidtext = ref('')
const loading = ref(false)
const type = ref(true)
const inputIP = ref('')
const imgurl = ref('')
const options = [
  {
    value: 'A',
    label: '环庆养殖场',
  },
  {
    value: 'B',
    label: '曹新庄养殖场',
  },
]
interface tableVideoData {
  data: string
  gallery: string
  id: string
}

const videoData = ref([
  {
    data: '12987122',
    gallery: 'Tom',
    id: '234',
  },
  {
    data: '12987122',
    gallery: 'Tom',
    id: '234',
  },
  {
    data: '12987122',
    gallery: 'Tom',
    id: '234',
  },
  {
    data: '12987122',
    gallery: 'Tom',
    id: '234',
  },
  {
    data: '12987122',
    gallery: 'Tom',
    id: '234',
  },
])

const initIDenv = () => {
  console.log('加载模型', galleryValue.value)
  if (galleryValue.value == '') {
    ElMessage({
      message: '请选择检索库',
      type: 'warning'
    })
  } else {
    console.log('radio', radio1.value)
    axios.get("/api/initenv?gallery=" + galleryValue.value).then((res) => {
      console.log(res.data)
      ElMessage({
        message: '加载模型成功',
        type: 'success'
      })
      active.value = 1
    })
  }
}
const changeDataSrc = () => {
  console.log('radio', radio1.value)
  if (radio1.value == '图 像') {
    type.value = true
  } else {
    type.value = false
  }
}
const handleChange = (file, fileList) => {
  console.log(file, fileList)
  curfile.value = file
  noneBtnImg.value = fileList.length > 0
}

const handleRemove = (file, fileList) => {
  noneBtnImg.value = false
  console.log(file, fileList)
}

const startimage = () => {
  console.log('开始识别')
  if (curfile.value == null) {
    ElMessage({
      message: '请选择图片',
      type: 'warning'
    })
  } else {
    const fileParam = new FormData()
    fileParam.append("file", curfile.value["raw"])
    fileParam.append("fileName", curfile.value["name"])
    axios.post('/api/uploadandinfer', fileParam).then(res => {
      console.log(res.data)
      imgidtext.value = res.data
      ElMessage({
        message: '识别成功',
        type: 'success'
      })
    }).catch(err => {
      console.log(err)
    })
    console.log(imgidtext)
  }
}
var timer
const swithchange = (val) => {
  console.log(loading.value)
  if (loading.value) {
    timer = setInterval(function () {
      // axios.get("/api/video_feed").then((response) => {
      //   console.log(response.data)
      //   imgurl.value = "data:image/jpeg;base64," + response.data["imgbase64"]
      // });
      //add new data
      videoData.value.push({
        data: '12987122',
        gallery: 'make',
        id: '1',
      })
    }, 1000);
  } else {
    window.clearInterval(timer);
  }
}
</script>


<style>
.left-card {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right-card {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-radio-button__inner {
  font-size: 16px;
  width: 100px;
}

.title {
  font-size: 40px;
  font-weight: bold;
  color: #21b3b9;
  align-items: center;
  justify-content: center;
  letter-spacing: 20px;
}

/* .el-row {
  margin-bottom: 40px;
} */


.disUoloadBtn .el-upload--picture-card {
  display: none;
  /* 上传按钮隐藏 */
}

.el-upload {
  width: 200px;
  height: 200px;
}

.displayType {
  display: none;
  /* 数据源类型 */
}
</style>