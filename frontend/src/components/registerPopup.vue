<template>
  <div class="register bsb">
    <p class="register_info tc">10秒快速注册，开启心动礼物兑换之旅!</p>
    <label class="register_label dib2 w100">
      <input class="register_ipt wh100" type="text" placeholder="请输入您的手机号" v-model="tel">
    </label>
    <label class="register_label flex w100">
      <input class="register_ipt wh100 fe" type="text" placeholder="请输入验证码" v-model="code">
      <i class="db register_validate" style="background-image:url(/static/img/validate.jpg)"></i>
    </label>
    <el-button class="register_submit bgc1 db nobd" round @click="fetchRegister">立即注册</el-button>
    <p class="register_already tc">已经注册 <a class="cor2" href="javascript:;">立即登录</a></p>
  </div>

</template>

<script>
  import { fetchRegister } from '@/api/api';
  import { checkPhone } from '@/assets/js/utils';

  export default {
    data(){
      return {
        tel: "",
        code: ""
      }
    },
    methods: {
      fetchRegister(){
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
        if(this.code==""){
          this.$message({
            type: 'error',
            message: '请输入验证码！'
          });
          return;
        }
        fetchRegister({ tel:this.tel,code:this.code }).then(res => {
          this.$message({
            type: 'success',
            message: res.info
          });
        });
      }
    }
  }
</script>

<style lang="less" scoped>
  .register{
    width: 7.2632rem;
    padding: 0 .7368rem;
    background-color: #fff;
  }
  .register_{
    &info{
      line-height: .7018rem;
      margin: .5263rem .2281rem;
      font-size: .2807rem;
      color: #666;
      background-color: #ffebce;
    }
    &alert{
      margin: 0 .2281rem;
    }
    &label{
      height: .7368rem;
      line-height: .7368rem;
      margin-top: .7719rem;
      border: 1px solid #e3e3e3;
      background-color: #fff;
    }
    &ipt{
      padding: 0 .2456rem;
      font-size: .2456rem;
    }
    &validate{
      width: 1.9298rem;
      background-size: auto 100%;
    }
    &submit{
      width: 88%;
      height: .8772rem;
      line-height: .8772rem;
      padding: 0;
      margin-top: 1.3158rem;
      margin-left: 6%;
      font-size: .3158rem;
      color: #fff;
      &:hover{
        background-color: #ff7e32;
      }
      &:active{
        background-color: #ff7e32;
      }
    }
    &already{
      margin: .4386rem 0 1.0526rem;
      font-size: .2807rem;
      color: #757575;
      a{
        margin-left: .2456rem; 
      }
    }
  }
</style>