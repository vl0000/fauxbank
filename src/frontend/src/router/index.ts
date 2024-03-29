import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import LoginPageVue from '@/views/LoginPage.vue';
import SignupPageVue from '@/views/SignupPage.vue';
import DashboardVue from '@/views/Dashboard.vue';
import SendVue from '@/views/Send.vue';
import ReceiveVue from '@/views/Receive.vue';
import ScanVue from '@/views/Scan.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/login'
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
  },
  {
    path:"/dashboard",
    name:"Dashboard",
    component: DashboardVue
  },
  {
    path:"/send",
    name: "Send",
    component: SendVue
  },
  {
    path:"/receive",
    name: "Receive",
    component: ReceiveVue
  },
  {
    path:"/scan",
    name: "Scan",
    component: ScanVue
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
