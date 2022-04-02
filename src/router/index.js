import Vue from 'vue'
import VueRouter from 'vue-router'
import LPage from '../views/LandingPage.vue'
import LoginPage from '../views/LoginPage.vue'
import SUp from '../views/SignUpPage.vue'
import HPage from '../views/HomePage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LPage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'Sign up',
    component: SUp
  },
  {
    path: '/home',
    name: 'Home',
    component: HPage
  }
]

const router = new VueRouter({
  routes
})

export default router
