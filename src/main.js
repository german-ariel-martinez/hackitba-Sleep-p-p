import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import './plugins/axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Para axios
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
