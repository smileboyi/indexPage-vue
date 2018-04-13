<template>
  <div class="login-bar bgctp w100">
    <img class="lb_logo pab hauto2" src="../assets/img/logo.png" alt="logo">
    <p class="lb_text pab">建立免费交换平台</p>
    <div class="lb_form fr h100 flex">
      <input class="lb_ipt" type="text" placeholder="手机号" v-model="tel">
      <input class="lb_ipt" type="password" placeholder="输入密码" v-model="password">
      <a class="lb_login-btn bgc1 dib tc" href="javascript:;" @click="fetchRegister">登录</a>
      <a class="lb_forget cor4 pre" href="javascript:;">忘记密码？</a>
    </div>
  </div>
</template>

<script>
  import { fetchLogin } from '@/api/api';
  import { checkPhone } from '@/assets/js/utils';


  export default {
    data(){
      return {
        tel: "",
        password: ""
      }
    },
    methods: {
      fetchRegister(){
        console.log(this.tel,this.password);
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
        
      }
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
      margin-right: 1.4035rem;
      align-items: center;
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
  }
</style>
