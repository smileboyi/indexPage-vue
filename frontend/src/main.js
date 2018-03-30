// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'

Vue.config.productionTip = false


// 使用ElementUI，按需加载
// import ElementUI from 'element-ui'
import { Button, InputNumber } from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(Button)
Vue.use(InputNumber)



// base.css
import './assets/css/wl.base.css' 


import axios from 'axios'


import App from './App'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})