<template>
  <div>
    <!-- <pageTop /> -->
    <el-row class="feature dn">
      <el-col :span="6" class="feature_item">
        <h3 class="cor5 feature_title tc cor5">
          <i class="icon feature_icon sn1 dib2"></i>量大
        </h3>
        <p class="feature_data">
          <span class="cor2">2000万+</span>高质量有效简历
        </p>
        <p class="feature_text">让您招人更靠谱</p>
      </el-col>
      <el-col :span="6" class="feature_item">
        <h3 class="cor5 feature_title tc cor5">
          <i class="icon feature_icon sn2 dib2"></i>人多
        </h3>
        <p class="feature_data">
          <span class="cor2">10000+</span>HR的聪明选择
        </p>
        <p class="feature_text">更多分享，更加活跃</p>
      </el-col>
      <el-col :span="6" class="feature_item">
        <h3 class="cor5 feature_title tc cor5">
          <i class="icon feature_icon sn3 dib2"></i>礼好
        </h3>
        <p class="feature_data"><span class="cor2">1000+</span>诱惑礼品
        </p>
        <p class="feature_text">请您开走法拉利</p>
      </el-col>
      <el-col :span="6" class="feature_item">
        <h3 class="cor5 feature_title tc cor5">
          <i class="icon feature_icon sn4 dib2"></i>周到
        </h3>
        <p class="feature_data">
          一站式人事招聘服务
        </p>
        <p class="feature_text">让您工作更轻松</p>
      </el-col>
    </el-row>
    <resumeBox />

    <!-- <pageBottom /> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import pageBottom from '@/components/pageBottom'
import pageTop from './pageTop'
import resumeBox from './resumeBox'


export default {
  components:{
    pageTop,
    resumeBox,
    pageBottom
  }
}
</script>

<style lang="less" scoped>
  .feature{
    height: 3.8596rem;
    border-bottom: .3333rem solid #f6f6f6;
  }
  .feature_{
    &item{
      margin-top: .57rem;
    }
    &title{
      line-height: 1.4;
      font-size: .5614rem;
      font-weight: 400;
    }
    &icon{
      position: relative;
      top: .1rem;
      width: .7193rem;
      height: .5965rem;
      margin-right: .386rem;
      background-image: url(../../assets/img/feature-icon.png);
      background-repeat: no-repeat;
      background-position-y: 0;
      &.sn1{
        top: .13rem;
        background-position-x: 0;
      }
      &.sn2{
        background-position-x: -.7193rem;
      }
      &.sn3{
        background-position-x: -1.4386rem;
      }
      &.sn4{
        background-position-x: -2.1579rem;
      }
    }
    &data{
      margin: .3035rem 0 .1057rem;
      font-size: .4211rem;
      text-align: center;
    }
    &text{
      font-size: .3158rem;
      text-align: center;
    }
  }


</style>
