import { Button,Form,FormItem,Input,Row,Col,Tabs,TabPane,Message } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Vue from 'vue'


Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Row)
Vue.use(Col)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.prototype.$message = Message;