import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue'
import LoginPageVue from '@/views/LoginPage.vue';
import SignupPageVue from '@/views/SignupPage.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage
  },
  {
    path:"/login",
    name: "Login",
    component: LoginPageVue
  },
  {
    path:"/signup",
    name:"Signup",
    component: SignupPageVue
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
