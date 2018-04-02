// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'

Vue.config.productionTip = false

// 使用element-ui
import { Button,Form,FormItem,Input } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)





// base.css
import './assets/css/wl.base.css' 

//使用axios
import axios from 'axios'


import App from './App'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})