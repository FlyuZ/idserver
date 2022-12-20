//引入vue
//引入vue-router
import { createRouter, createWebHashHistory } from "vue-router"
const router = createRouter({   //createRouter   vue2中是 new Vue
    history: createWebHashHistory(),
    routes: [
    { 
        path: '/',
        redirect: "/HelloWorld",
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
    },
    {
        name: 'Explain',
        path: '/Explain',
        component: () => import('../components/Explain.vue')
    },
    {
        path: '/:catchAll(.*)',
        component: () => import('../components/404.vue')
      }
    ]
})


export default router