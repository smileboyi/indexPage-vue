import Vue from 'vue';
import Vuex from 'vuex';
import home from './home';
import account from './account';


Vue.use(Vuex)


const createStore = () => {
  return new Vuex.Store({
    modules:{
      home,
      account
    }
  });
}
export default createStore;