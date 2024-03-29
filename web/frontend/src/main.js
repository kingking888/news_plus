// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import qs from 'qs'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import '@/css/iconfont/iconfont.css'

Vue.config.productionTip = false

Vue.use(ElementUI)

Vue.prototype.$ajax = axios
Vue.prototype.$qs = qs
// Vue.prototype.$host = 'http://127.0.0.1:5000'
Vue.prototype.$host = 'http://139.196.102.128:8000'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
