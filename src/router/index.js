import Vue from 'vue'
import VueRouter from 'vue-router'
import LPage from '../views/LandingPage.vue'
import LoginPage from '../views/LoginPage.vue'
import SUp from '../views/SignUpPage.vue'
import HPage from '../views/HomePage.vue'
import HPageFeed from '../views/HomePageFeed.vue'
import Vote from '../views/Vote.vue'
import CPost from '../views/CreatePost.vue'
import sotm from '../views/SOTM.vue'

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
    name: 'HomePage',
    component: HPage,
    children: [
      {
        path: 'feed',
        component: HPageFeed,
      },
      {
        path: 'vote',
        component: Vote,
      },
      {
        path: 'createpost',
        component: CPost,
      },
      {
        path: 'sotm',
        component: sotm,
      },
    ],
  }
]

const router = new VueRouter({
  routes
})

export default router
