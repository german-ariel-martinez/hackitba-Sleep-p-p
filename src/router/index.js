import Vue from 'vue'
import VueRouter from 'vue-router'
import LPage from '../views/LandingPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LPage
  }
]

const router = new VueRouter({
  routes
})

export default router
