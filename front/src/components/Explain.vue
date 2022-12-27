<template>
    <div>
        <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
        <h1>说明</h1>

        <el-row justify="center">
            <el-skeleton style="width:240px;  height:240px" :loading="loading" animated>
                <template #default>
                    <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
                </template>
                <template #template>
                    <el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
                        <!-- <canvas id="canvasid" width="240" height="240" style="background-color: #cccccc"></canvas> -->
                        <img style="width:240px;  height:240px" :src="imgurl" />
                    </el-card>
                </template>
            </el-skeleton>
        </el-row>
        <el-row justify="center">
            <el-col :span="12">
                <el-input v-model="inputIP" placeholder="Please input video IP" clearable />
            </el-col>
            <el-col :span="4">
                <el-switch v-model="loading" @change="swithchange" />
            </el-col>
        </el-row>
    </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import axios from "axios"
const loading = ref(false)
const inputIP = ref('')
const imgurl = ref('')
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