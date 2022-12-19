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
              <el-select v-model="value" class="m-2" placeholder="Select">
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
              <el-button type="primary" class="m-2" @click="loadModel">开始加载</el-button>
            </el-col>
          </el-row>
        </el-aside>
        <el-main width="60%">
          <el-row>
            <!-- drag action="/apis/uploadImage"   -->
            <el-col :span="12">
            <!-- <el-upload class="upload-img" drag action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15" imageUrl="false" :limit="1"
              accept="image/png, image/jpeg, image/jpg" :file-list="fileList" list-type="picture"
              :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload"></el-upload> -->
              <el-upload action="#" list-type="picture-card" accept="image/png, image/jpeg, image/jpg" :limit="1" :auto-upload="false" :on-success="handleAvatarSuccess">
                <el-icon><Plus /></el-icon>
              </el-upload>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </div>
  </div>

</template>



<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
const active = ref(0)
const value = ref('')
const options = [
  {
    value: 'Option1',
    label: 'Option1',
  },
  {
    value: 'Option2',
    label: 'Option2',
  },
]
const radio1 = ref('图像')
const loadModel = () => {
  console.log('加载模型', value.value)
  if (value.value == '') {
    ElMessage({
      message: '请选择检索库',
      type: 'warning'
    })
  } else {
    active.value++
    ElMessage({
      message: '开始加载',
      type: 'success'
    })
  }
}
const fileList = ref([])
const handleAvatarSuccess = (res, file) => {
  if (res == "success") {
    fileList.value = fileList.value.concat(file)
    console.log('fileList', fileList.value)
  }
}
const beforeAvatarUpload = (file) => {
  const isJPG = file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/jpg'
  const isLt2M = file.size / 1024 / 1024 < 2
  if (!isJPG) {
    ElMessage.error('上传图片只能是 JPG、PNG、JPG 格式!')
  }
  if (!isLt2M) {
    ElMessage.error('上传图片大小不能超过 2MB!')
  }
  return isJPG && isLt2M
}
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
</style>