//引入vue
//引入vue-router
import { createRouter, createWebHashHistory } from "vue-router"
const router = createRouter({   //createRouter   vue2中是 new Vue
    history: createWebHashHistory(),
    routes: [{  //配置路由规则
        name: 'HelloWorld',
        path: '/', //默认路径
        component: () => import('../components/HelloWorld.vue')
    },
    {
        name: 'HelloWorld',
        path: '/HelloWorld', 
        component: () => import('../components/HelloWorld.vue')
    },
    {
        name: 'Index',
        path: '/Index',
        component: () => import('../components/Index.vue')
    },
    {
        name: 'ID',
        path: '/ID',
        component: () => import('../components/ID.vue')
    }
    ]
})


export default router