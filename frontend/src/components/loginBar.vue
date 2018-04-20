<template>
  <div class="login-bar bgctp w100">
    <img class="lb_logo pab hauto2" src="../assets/img/logo.png" alt="logo">
    <p class="lb_text pab">建立免费交换平台</p>
    <div :class="{ 'lb_form':true, 'dn':account.loginState }">
      <input class="lb_ipt" type="text" placeholder="手机号" v-model="tel">
      <input class="lb_ipt" type="password" placeholder="输入密码" v-model="password" @keyup.enter="fetchAccountLogin">
      <a class="lb_login-btn bgc1 dib tc" href="javascript:;" @click="fetchAccountLogin">登录</a>
      <a class="lb_forget cor4 pre" href="javascript:;">忘记密码？</a>
    </div>
    <p :class="{ 'lb_user':true, 'dn':!account.loginState }">
      <!-- 进入/account/index后，再通过tel加载用户信息，填充的容器上。不写成/account/152...形式 -->
      <a class="lb_link" href="/account/index">{{ tel | telNumberHide }}</a>，欢迎回来  
      （<span class="lb_out" @click="fetchAccountLogout">注销</span>）
    </p>
  </div>
</template>

<script>
  import { fetchLogin } from '@/api/api';
  import { checkPhone } from '@/assets/js/utils';
  import { telNumberHide } from '@/assets/js/filters';
  import { mapState, mapMutations } from 'vuex'


  export default {
    data(){
      return {
        tel: "",
        password: ""
      }
    },
    computed: {
      ...mapState(['account'])
    },
    methods: {
      ...mapMutations('account', [
        'turnloginState',
        'turnlogoutState'
      ]),
      fetchAccountLogin(){
        if(this.tel==""){
          this.$message({
            type: 'error',
            message: '请输入手机号！'
          });
          return;
        }
        if(!checkPhone(this.tel)){
          this.$message({
            type: 'error',
            message: '手机号输入有误！'
          });
          return;
        }
        if(this.password==""){
          this.$message({
            type: 'error',
            message: '请输入密码！'
          });
          return;
        }
        fetchLogin({ tel:this.tel,password:this.password }).then(res => {
          if(res.error){
            this.$message({
              type: "error",
              message: res.error
            });
          }else{
            // 可以返回一个用户id或者用户昵称，这里直接用tel显示用户
            this.$message({
              type: "success",
              message: res.info
            });
            this.turnloginState({token:res.token});

            // 持久化登录，或者用cookie。否则页面刷新，重新登录
            // localStorage.setItem("login_token",res.token);
            // localStorage.setItem("account_tel",this.tel);
          }
        });
      },
      fetchAccountLogout(){
        this.turnlogoutState();
      }
    },
    filters: {
      telNumberHide
    }
  }
</script>

<style lang="less" scoped>
  .login-bar{
    height: 1.6667rem;
  }
  .lb_{
    &logo{
      left: .9649rem;
      width: 2.4211rem;
      height: .8421rem;
    }
    &text{
      left: 3.6842rem;
      top: .57rem;
      font-size: .2832rem;
      color: #fff;
    }
    &form{
      display: -webkit-flex;
      display: flex;
      -webkit-justify-content: space-between;
      justify-content: space-between;
      float: right;
      height: 100%;
      margin-right: 1.4035rem;
      align-items: center;
    }
    &form.dn{
      display: none;
    }
    &ipt{
      width: 3.1579rem;
      height: .5789rem;
      padding: 0 .3509rem;
      margin-right: .2em;
      line-height: .5789rem;
      font-size: 12px;
      color: #fff;
      letter-spacing: 2px;
      background-color: #202223;
    }
    &login-btn{
      width: .9474rem;
      height: .5289rem;
      line-height: .5289rem;
      font-size: .2456rem;
      color: #fff;
    }
    &forget{
      top: .1rem;
      left: .2456rem;
      font-size: 12px;
      text-decoration: underline;
    }
    &user{
      position: absolute;
      right: 1.4035rem;
      padding-top: .57rem;
      height: 100%;
      font-size: .32rem;
      color: #ccc;
      -webkit-box-sizing: border-box;
	    box-sizing: border-box;
    }
    &link{
      color: #ccc;
    }
    &link:hover{
      color: #fff;
      cursor: pointer;
    }
    &out{
      color: #d8454b;
    }
  }
</style>
