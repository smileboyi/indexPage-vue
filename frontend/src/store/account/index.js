export default {
  namespaced: true,
  state: {  
    loginState: false,
    token: ""
  },  
  mutations: {
    // 登录
    turnloginState(state, data) {
      state.loginState = true;
      state.token = data.token;
    },
    // 注销
    turnlogoutState(state) {
      state.loginState = false;
      state.token = "";
    },
  },
  actions: {

  }
}