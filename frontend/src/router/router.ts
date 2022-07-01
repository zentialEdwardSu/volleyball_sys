import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import main from "../components/index.vue"
const routes = [
  {
    path: '',
    // name: 'home',
    redirect: '/w/workbench'
  },

    {
      path:"/w",
      name:"主页面",
      component:main,
      children:[
        {
          path: "/w/workbench",
          name:"workbench",
          component: ()=>import('../views/workbench/index.vue')
        },
        {
          path:"/w/setting",
          name:"setting",
          component:()=>import("../views/setting/index.vue")
        },
        {
          path:"/w/about",
          name:"About",
          component:()=>import("../views/AboutView.vue")
        }
      ]
    },
    {
      path:"/about",
      name:"test",
      component:()=>import("../views/AboutView.vue")
    }

]

const router = createRouter({
  history: createWebHistory(),
  routes:routes
})

export default router
