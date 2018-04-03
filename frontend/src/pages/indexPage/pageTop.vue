<template>
  <div class="page-top pre contain" style="background-image: url(/static/img/car-bg.jpg)">
    <loginBar class="pt_login-bar pab not" />
    <div class="left pab hauto2">
      <p class="ptl_text1">只要你是HR 分享简历资源</p>
      <p class="ptl_text2">法拉利送给你！</p>
      <div class="ptl_dots pre">
        <i class="ptl_dot"><i></i></i>
        <i class="ptl_dot"><i></i></i>
        <i class="ptl_dot ac"><i></i></i>
        <span class="ptl_choose"><i class="ptl_line dib pre"></i>Choose Color</span>
      </div>
      <div class="ptl_num">100,000,000 优悦钱</div>
      <el-button class="ptl_btn" round>立即兑换</el-button>
    </div>
    <registerPopup class="pab pb_register-popup hauto2" />
  </div>
</template>

<script>
import loginBar from '@/components/loginBar'
import registerPopup from '@/components/registerPopup'


export default {
  components:{
    loginBar,
    registerPopup
  }
}
</script>

<style lang="less" scoped>
  .page-top{
    height: 13.193rem;
    .left{
      left: 3.8596rem;
    }
  }
  .ptl_{
    &text1{
      line-height: 1.4;
      font-size: .6315rem;
      color: #fff;
    }
    &text2{
      line-height: 1.4;
      font-size: 1rem;
      color: #df5930;
    }
    &dots{
      z-index: 10;
    }
    &dot{
      display: inline-block;
      position: relative;
      width: .3684rem;
      height: .3684rem;
      border-radius: 50%;
      background-color: #362d2f;
      z-index: 10;
      i{
        position: absolute;
        bottom: 0;
        right: 0;
        left: 0;
        top: 0;
        margin: auto;
        display: inline-block;
        width: .2631rem;
        height: .2631rem;
        border-radius: 50%;
      }
      &:nth-of-type(1) i{
        background-color: #d3d4d3;
      }
      &:nth-of-type(2) i{
        background-color: #d4b11a;
      }
      &:nth-of-type(3) i{
        background-color: #a41213;
      }
      &.ac{
        transform: scale(1.2);
      }
    }
    &line{
      top: -.3em;
      width: 10px;
      height: 1px;
      margin-right: 8px;
      background-color: #504b5d;
    }
    &choose{
      font-size: .3684rem;
      color: #6f686f;
    }
    &num{
      line-height: 1;
      margin-top: .7018rem;
      margin-bottom: .5263rem;
      font-size: .6316rem;
      color: #fff;
    }
    &btn{
      width: 2.8947rem;
      line-height: .8246rem;
      padding: 0;
      font-size: .3158rem;
      color: #b6b6b6;
      border-color: #9e9e9e;
      background-color: transparent;
    }
  }
  .pb_register-popup{
    right: 1.4035rem;
  }
</style>
