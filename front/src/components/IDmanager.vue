<template>
    <div class="common-layout" style="height:100%">
        <el-container>
            <el-header class="title">
                <el-row>
                    <el-col :span="4"><img style="height:60px" alt="nwafu logo" src="../assets/nwafu.png" /></el-col>
                    <el-col :span="14">羊只个体身份管理系统</el-col>
                    <el-col :span="6"><img style="height:60px" alt="sheep logo"
                            src="../assets/icon-sheep.png" /></el-col>
                </el-row>
            </el-header>
            <el-container>
                <el-aside width="40%" style="padding:10px;">
                    <el-card shadow="always" style="height: 300px;">
                        <el-table :data="GalleryInfo" style="width: 100%">
                            <el-table-column prop="gallery" label="Gallery" />
                            <el-table-column prop="name" label="Name" />
                            <el-table-column label="Operations">
                                <template #default="scope">
                                    <el-button link type="primary" size="small"
                                        @click="Detail(scope.$index, scope.row)">查看详情</el-button>
                                    
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-card>
                </el-aside>
                <el-main width="60%" style="padding:10px">
                    <el-card shadow="always" style="height: 300px;">
                        <el-table :data="IDInfo" style="width: 100%">
                            <el-table-column prop="gallery" label="Gallery" />
                            <el-table-column prop="id" label="ID" />
                            <el-table-column prop="info" label="Info" />
                            <el-table-column label="Operations">
                                <template #default="scope">
                                    <el-button link type="primary" size="small"
                                        @click="Edit(scope.$index, scope.row)">编辑</el-button>
                                    <el-button link type="primary" size="small"
                                        @click="Delete(scope.$index, scope.row)">删除</el-button>
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
interface ID {
    gallery: string
    id: string
    info: string
}
interface Gallery {
    gallery: string
    name: string
}

const Detail = (index: number, row: Gallery) => {
    console.log('click')
}
const Delete = (index: number, row: ID) => {
    console.log('click')
}
const Edit = (index: number, row: ID) => {
    console.log('click')
}

const IDInfo: ID[] = [
    {
        gallery: '104016',
        id: '1',
        info: '',
    },
    {
        gallery: '104016',
        id: '2',
        info: '',
    },
    {
        gallery: '104016',
        id: '3',
        info: '',
    },
    {
        gallery: '104016',
        id: '4',
        info: '',
    },
    {
        gallery: '104016',
        id: '5',
        info: '',
    },

]
const GalleryInfo: Gallery[] = [
    {
        gallery: '104016',
        name: '环庆养殖场'
    },
    {
        gallery: '104017',
        name: '环庆养殖场'
    },
    {
        gallery: '102006',
        name: '曹新庄养殖场'
    },
    {
        gallery: '102007',
        name: '曹新庄养殖场'
    },
]
</script>

<style>
.left-card-manager {
padding: 5px;
  border-radius: 5px;
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right-card-manager {
padding: 5px;
    border-radius: 5px;
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.title {
  font-size: 40px;
  font-weight: bold;
  color: #21b3b9;
  align-items: center;
  justify-content: center;
  letter-spacing: 20px;
}

</style>