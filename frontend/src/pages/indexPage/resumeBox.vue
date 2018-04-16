<template>
  <div class="resume">
    <h2 class="resume_title tc">
      <span class="cor2">2000万+</span>
      简历数据，唾手可得
    </h2>
    <label class="resume_search bgc4 flex wauto">
      <input class="resume_search-ipt fe" type="text" placeholder="更多优质简历搜索">
      <a class="resume_search-btn pre" href="javascript:;">
        <img class="resume_search-icon centre2" src="../../assets/img/search.png" alt="">
      </a>
    </label>
    <div class="resume_show-box icon" style="background-image: url(./static/img/track-bg.jpg)">
      <div class="resume_show-box flex tc">
        <div class="grail fe resume_show-item--left">
          <div class="flex fe">
            <div class="fe resume_flex--black">
              <p class="resume_show-name">CEO经理</p>
              <p class="resume_show-num">1,230,101</p>
            </div>
            <div class="fe resume_flex--gray">
              <p class="resume_show-name">COO</p>
              <p class="resume_show-num">2,000,561</p>
            </div>
          </div>
          <div class="flex fe">
            <div class="fe resume_flex--black2">
              <p class="resume_show-name">桥梁工程师</p>
              <p class="resume_show-num">1,230,101</p>
            </div>
            <div class="fe resume_flex--black3">
              <p class="resume_show-name">Android架构师</p>
              <p class="resume_show-num">2,000,561</p>
            </div>
          </div>
          <div class="flex fe">
            <div class="fe resume_flex--orange2">
              <p class="resume_show-name">五金产品总监</p>
              <p class="resume_show-num">1,230,101</p>
            </div>
            <div class="fe resume_flex--black4">
              <p class="resume_show-name">BD</p>
              <p class="resume_show-num">7,000,561</p>
            </div>
          </div>
        </div>

        <div class="grail fe resume_show-item--center">
          <div class="flex fe">
            <div class="resume_show-item--md resume_flex--black">
              <p class="resume_show-name">区块链研发工程师</p>
              <p class="resume_show-num">3,890,004</p>
            </div>
            <div class="fe resume_flex--orange">
              <p class="resume_show-name">总经理</p>
              <p class="resume_show-num">90,070</p>
            </div>
          </div>
          <div class="flex fe">
            <div class="resume_show-item--lg">
              <div class="bg h100">
                <p class="resume_show-name">CEO/总经理</p>
                <p class="resume_show-num">65,890,004</p>
              </div>
            </div>
          </div>
          <div class="flex fe">
            <div class="fe resume_flex--gray4">
              <p class="resume_show-name">SQLSEVER工程师</p>
              <p class="resume_show-num">3,890,004</p>
            </div>
            <div class="resume_show-item--md resume_flex--black">
              <p class="resume_show-name">Marketing Specialist</p>
              <p class="resume_show-num">90,070</p>
            </div>
          </div>
        </div>

        <div class="grail fe resume_show-item--right">
          <div class="flex fe">
            <div class="fe resume_flex--black">
              <p class="resume_show-name">财务总监</p>
              <p class="resume_show-num">12,230,101</p>
            </div>
            <div class="fe resume_flex--gray2">
              <p class="resume_show-name">CEO助理</p>
              <p class="resume_show-num">33,230,101</p>
            </div>
          </div>
          <div class="flex fe">
            <div class="fe resume_flex--black3">
              <p class="resume_show-name">知识产权顾问</p>
              <p class="resume_show-num">3,230,101</p>
            </div>
            <div class="fe resume_flex--black">
              <p class="resume_show-name">CTO</p>
              <p class="resume_show-num">3,230,101</p>
            </div>
          </div>
          <div class="flex fe">
            <div class="fe resume_flex--gray3">
              <p class="resume_show-name">语音识别研究员</p>
              <p class="resume_show-num">12,230,101</p>
            </div>
            <div class="fe resume_flex--black">
              <p class="resume_show-name">BI产品架构师</p>
              <p class="resume_show-num">33,230,101</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {

  }
</script>

<style lang="less" scoped>
  .resume{
    padding-top: 1.5263rem;
  }
  .resume_{
    &title{
      font-size: .5965rem;
      font-weight: 400;
    }
    &search{
      width: 10.9123rem;
      height: .8772rem;
      margin-top: .5965rem;
      margin-bottom: 1.1754rem;
      border-radius: .4386rem;
    }
    &search-ipt{
      padding-left: .6316rem;
      padding-right: 10px;
      font-size: .2807rem;
      &::-moz-placeholder{
        color: #c8c8c8;
      }
      &::-ms-input-placeholder{
        color: #c8c8c8;
      }
      &::-webkit-input-placeholder{
        color: #c8c8c8;
      }
    }
    &search-btn{
      width: .4386rem;
      height: .4386rem;
      padding: 5px 0;
      padding-left: .5614rem;
      align-self: center;
      margin-right: .3614rem;
      border-left: 1px solid #eaebeb;
    }
    &search-icon{
      width: .4386rem;
      height: .4386rem;
    }
  }

  .resume_show-box{
    height: 15.0175rem;
    font-size: .4211rem;
    color: #fff;
  }
  .resume_show-item--md{
    width: 8.772rem;
  }
  .resume_show-item--lg{
    position: relative;
    width: 13.3543rem;
    color: #222;
    background-color: #fff;
    &::after,&::before,
    .bg:after,.bg::before{
      content: '';
      display: block;
      position: absolute;
      width: .3333rem;
      height: .3333rem;
      background-image: url(../../assets/img/adorn.png);
      background-size: 100% auto;
    }
    &::after{
      content: '';
      top: 10px;
      left: 10px;
      transform: rotate(90deg);
    }
    &::before{
      content: '';
      bottom: 10px;
      left: 10px;
    }
    .bg:after{
      content: '';
      top: 10px;
      right: 10px;
      transform: rotate(180deg);
    }
    .bg::before{
      bottom: 10px;
      right: 10px;
      transform: rotate(-90deg);
    }
    .resume_show-name{
      margin-top: 0;
      padding-top: 1.8421rem;
    }
  }
  .resume_show-name{
    line-height: 1.4;
    margin-top: 1.8421rem;
  }
  .resume_show-num{
    line-height: 1.4;
    margin-top: .4863rem;
  }
  .resume_flex--black{
    background-color: rgba(0, 0, 0, .7);
  }
  .resume_flex--black2{
    background-color: rgba(31, 31, 31, .9);
  }
  .resume_flex--black3{
    background-color: rgba(0, 0, 0, .3);
  }
  .resume_flex--black4{
    background-color: rgba(0, 0, 0, .7);
  }
  .resume_flex--gray{
    color: #222;
    background-color: rgba(228, 228, 228, .9);
  }
  .resume_flex--gray2{
    color: #222;
    background-color: rgba(200, 200, 200, .5);
  }
  .resume_flex--gray3{
    color: #222;    
    background-color: rgba(255, 255, 255, .7);
  }
  .resume_flex--gray4{
    color: #222;
    background-color: rgba(255, 255, 255, .6);
  }
  .resume_flex--orange{
    background-color: rgba(217, 106, 48, .9);
  }
  .resume_flex--orange2{
    background-color: rgba(217, 106, 48, .85);
  }
</style>
