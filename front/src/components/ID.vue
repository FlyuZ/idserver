<template>
  <div>
    <el-row>
      <el-col :span="24">
        <el-steps :active="active" finish-status="success" simple>
          <el-step title="配置" />
          <el-step title="识别" />
        </el-steps>
      </el-col>
    </el-row>
    <div class="common-layout">
      <el-container>
        <el-aside width="40%">
          <el-row>
            <el-col :span="8">选择检索库</el-col>
            <el-col :span="16">
              <el-select v-model="galleryValue" class="m-2" placeholder="Select">
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
              </el-select>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">选择数据源</el-col>
            <el-col :span="16">
              <el-radio-group v-model="radio1">
                <el-radio-button label="视频流" disabled />
                <el-radio-button label="图像" selected />
              </el-radio-group>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-button type="primary" class="m-2" @click="initIDenv">开始加载</el-button>
            </el-col>
          </el-row>
        </el-aside>

        <el-main width="60%">
          <el-row justify="center">
            <el-col :span="24">
              <el-upload :class="{ disUoloadBtn: noneBtnImg }" action="#" list-type="picture-card" accept="image/*"
                :limit="1" :auto-upload="false" :on-remove="handleRemove" :on-change="handleChange">
                <el-icon>
                  <Plus />
                </el-icon>
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
              <el-button type="primary" class="m-2" @click="start">开始识别</el-button>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </div>
  </div>

</template>



<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import { ElMessage, UploadProps } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import axios from "axios"

const active = ref(0)
const galleryValue = ref('')
const radio1 = ref('图像')
const noneBtnImg = ref(false)
const curfile = ref(null)
const idtext = ref('')
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
    console.log('option', options)
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

const handleChange = (file, fileList) => {
  console.log(file, fileList)
  curfile.value = file
  noneBtnImg.value = fileList.length > 0
}

const handleRemove = (file, fileList) => {
  noneBtnImg.value = false
  console.log(file, fileList)
}

const start = () => {
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
</script>


<style>
.el-row {
  margin-bottom: 50px;
}

/* .el-row:first-child {
  margin-bottom: 50px;
} */

.el-row:last-child {
  margin-bottom: 0;
}

.disUoloadBtn .el-upload--picture-card {
  display: none;
  /* 上传按钮隐藏 */
}
</style>