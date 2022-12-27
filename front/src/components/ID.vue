<template>
  <div class="common-layout" style="height:100%">
    <el-container>
      <el-aside width="35%">
        <el-row>
          <el-col :span="24">
            <div class="grid-content">配置
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">选择检索库</el-col>
          <el-col :span="16">
            <el-select v-model="galleryValue" placeholder="Select">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">选择数据源</el-col>
          <el-col :span="16">
            <el-radio-group v-model="radio1" @change="changeDataSrc">
              <el-radio-button label="视频流" />
              <el-radio-button label="图像" selected />
            </el-radio-group>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <el-button type="primary" @click="initIDenv">开始加载</el-button>
          </el-col>
        </el-row>
      </el-aside>

      <el-main width="65%" style="border-left:1px black solid; padding: 0">
        <el-row>
          <el-col :span="24">
            <div class="grid-content">识别
            </div>
          </el-col>
        </el-row>
        <div class="imageid" :class="{ displayType: !type }">
          <el-row justify="center">
            <el-col :span="24">
              <el-upload :class="{ disUoloadBtn: noneBtnImg }" action="#" list-type="picture-card" accept="image/*"
                :limit="1" :auto-upload="false" :on-remove="handleRemove" :on-change="handleChange">
                <el-icon class="el-icon--upload" :size="50"><upload-filled /></el-icon>
              </el-upload>
            </el-col>
          </el-row>
          <el-row justify="center">
            <el-col :span="16" v-model="idtext">
              {{ idtext }}
            </el-col>
          </el-row>
          <el-row justify="center">
            <el-col :span="24">
              <el-button type="primary" @click="startimage">开始识别</el-button>
            </el-col>
          </el-row>
        </div>

        <div class="videoid" :class="{ displayType: type }">
          <el-row justify="center">
            <el-skeleton style="width: 240px" :loading="loading" animated>
              <template #default>
                <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
              </template>
              <template #template>
                <el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
                  <img style="width:240px;  height:240px" :src="imgurl" />
                </el-card>
              </template>
            </el-skeleton>
          </el-row>
          <el-row justify="center">
            <el-col :span="16" v-model="idtext">
              {{ idtext }}
            </el-col>
          </el-row>

            <el-row justify="center"> 
              <el-col :span="12">
                <el-input v-model="inputIP" placeholder="请输入IP地址，开始识别" clearable />
              </el-col>
              <el-col :span="4">
                <el-switch v-model="loading"   @change="swithchange"/>
              </el-col>
            </el-row>
          
        </div>
      </el-main>
    </el-container>
  </div>

</template>



<script lang="ts" setup>
import { ref} from "vue";
import { ElMessage, UploadProps } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { UploadFilled } from '@element-plus/icons-vue'
import axios from "axios"

const active = ref(0)
const galleryValue = ref('')
const radio1 = ref('图像')
const noneBtnImg = ref(false)
const curfile = ref(null)
const idtext = ref('')
const loading = ref(false)
const type = ref(true)
const inputIP = ref('')
const imgurl = ref('')
const options = [
  {
    value: 'A',
    label: '环庆',
  },
  {
    value: 'B',
    label: '曹新庄',
  },
]

const initIDenv = () => {
  console.log('加载模型', galleryValue.value)
  if (galleryValue.value == '') {
    ElMessage({
      message: '请选择检索库',
      type: 'warning'
    })
  } else {
    console.log('radio', radio1.value)
    axios.post("/api/initIDenv").then((res) => {
      console.log('res', res)
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
  if (radio1.value == '图像') {
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
    axios.post('/api/uploadAndInfer', fileParam).then(res => {
      console.log(res)
      ElMessage({
        message: '识别成功',
        type: 'success'
      })
    }).catch(err => {
      console.log(err)
    })
    idtext.value = 'ID: 100'
    console.log(idtext)
  }
}
var timer
const swithchange = (val) => {
    console.log(loading.value)
    if (loading.value) {
        timer = setInterval(function () {
            axios.get("/api/video_feed").then((response) => {
                console.log(response.data)
                imgurl.value = "data:image/jpeg;base64," + response.data["imgbase64"]
            });
        }, 1000);
    } else {
        window.clearInterval(timer);
    }
}
</script>


<style>
.el-row {
  margin-bottom: 50px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.disUoloadBtn .el-upload--picture-card {
  display: none;
  /* 上传按钮隐藏 */
}
.el-upload{
  width: 240px;
  height: 240px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
  background-color: gray;
  line-height: 36px;
  color: #fff;
}

.displayType {
  display: none;
  /* 数据源类型 */
}
</style>