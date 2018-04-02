<template>
  <div class="register">
    <label class="register_label dib2">
      <input class="register_ipt wh100" type="text" placeholder="请输入您的手机号">
    </label>
    <label class="register_label dib2">
      <input class="register_ipt wh100" type="text" placeholder="请输入验证码">
    </label>
    <el-button class="register_submit" round>立即注册</el-button>
    <p class="register_already">已经注册 <a class="cor2" href="javascript:;">立即登录</a></p>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          code: ''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>

<style lang="less" scoped>
  .register{
    width: 7.2632rem;
  }
  .register_{
    &label{
      height: .7368rem !important;
      line-height: .7368rem;
      border-radius: 1px solid #e3e3e3;
      background-color: #fff;
    }
    &ipt{
      font-size: .2456rem;

    }
    &submit{

    }
    &already{

    }
  }
</style>
