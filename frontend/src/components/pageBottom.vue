<template>
  <div class="page-bottom">
    <div class="top bgc1 pre">
      <img class="pbt_img pab hauto2" src="../assets/img/dialogue.png" alt="">
      <el-button class="pbt_btn nobd pab hauto2 cor2" round>立即注册</el-button>
    </div>
    <div class="center flex">
      <img class="pbc_left" src="../assets/img/qubiezhen.png" alt="">
      <div class="pbc_center fe">
        <h3 class="pbc_title cor5">
          人事助理APP
          <h4 class="pbc_url dib">WWW.QBZRS.COM</h4>
        </h3>
        <P class="pbc_slogan cor4">一款让中小企业将管理快速执行，轻便免费的APP</P>
      </div>
      <div class="pbc_right">
        <img class="pbc_qrcode" src="../assets/img/QR-code.jpg" alt="">
        <span class="pbc_text flex centre3 tc flex">扫描免费下载</span>
      </div>
    </div>
    <div class="bottom bgc3 tc">
      <div class="pbb_links dib2">
        <a class="pbb_link" href="javascript:;">联系我们</a>
        <a class="pbb_link" href="javascript:;">关于我们</a>
        <a class="pbb_link" href="javascript:;">法律申明</a>
        <a class="pbb_link" href="javascript:;">优小招介绍</a>
        <a class="pbb_link noaf" href="javascript:;">帮助中心</a>
      </div>
      <div class="pbb_list">
        <span class="pbb_item">Copyright 2017 优纳科技集团</span>
        <span class="pbb_item">渝ICP备16888888号-1</span>
        <span class="pbb_item">人才服务许可证:RC8888888</span>
        <span class="pbb_item">©2016 优小招 版权所有</span>
      </div>
      <div class="pbb_icons dib2">
        <i class="pbb_icon icon dib2"></i>
        <i class="pbb_icon icon dib2"></i>
        <i class="pbb_icon icon dib2"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
  .page-bottom{
    .top{
      height: 2.9474rem;
    }
    .center{
      height: 5.2632rem;
      
    }
    .bottom{
      height: 4.9123rem;
    }
  }
  .pbt_{
    &img{
      left: 2.2982rem;
      width: 10.0702rem;
      height: 1.4385rem;
    }
    &btn{
      right: 2.8421rem;
      width: 3.8596rem;
      height: 1.1053rem;
      font-size: .4211rem;
    }
  }
  .pbc_{
    &left{
      width: 3.7544rem;
      height: 1.1579rem;
      margin-left: 2.7544rem;
      align-self:center;      
    }
    &center{
      margin-left: 3.0877rem;
      align-self:center;      
    }
    &title{
      font-size: .6965rem;
      font-weight: 500;
    }
    &url{
      font-size: .4211rem;
      font-weight: 300;
    }
    &slogan{
      font-size: .3509rem;
    }
    &right{
      margin-right: 3.7368rem;
      align-self:center;      
    }
    &qrcode{
      width: 2.3158rem;
      height: 2.3158rem;
    }
    &text{
      margin-top: .3211rem;
      font-size: .3156rem;
      letter-spacing:.05rem;
      justify-content:center;
    }
  }
  .pbb_{
    &links{
      margin-top: 1.5789rem;
    }
    &link{
      display: inline-block;
      position: relative;
      padding: 0 1.3em;
      font-size: .2856rem;
      color: #878787;
      &::after{
        content: "";
        display: inline-block;
        position: absolute;
        right: 0;
        top: 10%;
        height: 80%;
        width: 1px;
        background-color: #878787;
      }
    }
    &list{
      margin-top: -.5em;
      font-size: .2356rem;
      color: #878787;
    }
    &item{
      margin-right: .2807rem;
      &:last-of-type{
        margin-right: 0;
      }
    }
    &icons{
      margin-top: .5263rem;
    }
    &icon{
      width: .6842rem;
      height: .6842rem;
      margin-right: .5263rem;
      background-image: url(../assets//img/contact.png);
      background-position-y: 0;
      &:nth-of-type(1){
        background-position-x: 0;
      }
      &:nth-of-type(2){
        background-position-x: -.6892rem;
      }
      &:nth-of-type(3){
        margin-right: 0;
        background-position-x: -1.3984rem;
      }
    }
  }

</style>
