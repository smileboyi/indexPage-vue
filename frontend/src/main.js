// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from '@/router'
import store from '@/store';

Vue.config.productionTip = false

//开启mock(如果用的是后台数据，不是mock数据，去掉)
import Mock from '@/mock';
Mock.start();


// 使用element-ui
import { Button,Form,FormItem,Input,Row,Col,Tabs,TabPane } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Row)
Vue.use(Col)
Vue.use(Tabs)
Vue.use(TabPane)

// 使用VueVideoPlayer
import VueVideoPlayer from 'vue-video-player'
import 'video.js/dist/video-js.css'
Vue.use(VueVideoPlayer)

// base.css
import './assets/css/wl.base.css' 

//使用axios
import axios from 'axios'

import App from './App'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }  
})