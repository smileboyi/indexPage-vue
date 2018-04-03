<template>
  <div class="gift">
    <div class="gift_top">
      <h2 class="gift_title tc">
        <span class="cor2">1000+礼品</span>
        源自法拉利的诱惑
      </h2>
      <p class="gift_text tc">
        已有<span class="cor2">16900人</span>兑换礼品
      </p>
    </div>
    <el-tabs class="nobd" type="border-card" v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="10000以上" name="1wup">
        <div class="gift_group flex">
          <div class="gift_item--big pre">
            <i class="icon image dib2" style="background-image: url(/static/img/red-car.jpg)"></i>
            <div class="main tc dib pab hauto2">
              <h4 class="title">法拉利488</h4>
              <div class="price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="price--discount">
                <span>优</span>30000元
              </div>
              <a class="link db tc wauto" href="javascript:;">去兑换</a>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
        </div>

        <div class="gift_group flex">
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
          <div class="fe gift_item">
            <img class="gift_item-img" src="/static/img/product.jpg" alt="">
            <div class="gift_item-main">
              <h4 class="gift_item-title">Apple MacBook Pro 15.4英寸笔记本电脑</h4>
              <p class="gift_item-parameter">银色(Core i7 处理器/16GB内存/256GB</p>
              <div class="gift_item-price--market">
                <span>市值</span>￥36890元
              </div>
              <div class="gift_item-price--discount">
                <span>优</span>30000元
              </div>
            </div>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="8000以上" name="8kup">8000以上</el-tab-pane>
      <el-tab-pane label="6000以上" name="6kup">6000以上</el-tab-pane>
      <el-tab-pane label="4000以上" name="4kup">4000以上</el-tab-pane>
      <el-tab-pane label="3000以上" name="3kup">3000以上</el-tab-pane>
      <el-tab-pane label="2000以上" name="2kup">2000以上</el-tab-pane>
      <el-tab-pane label="1000以上" name="1kup">1000以上</el-tab-pane>
      <el-tab-pane label="1000以下" name="1kdown">1000以下</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
 export default {
    data() {
      return {
        activeName: '1wup'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
  };
</script>

<style lang="less" scoped>
  .gift{
    border-bottom: 1.0526rem solid #222;
  }
  .gift_{
    &top{
      padding: 2.0702rem 0 1.4035rem;
      background-color: #222;
    }
    &title{
      font-size: .5965rem;
      font-weight: 400;
      color: #fff;
    }
    &text{
      margin-top: .4561rem;
      font-size: .4211rem;
      color: #fff;
    }
    &group{
      height: 8.2456rem;
    }
    &item{
      width: 20%;
      box-sizing: border-box;
      border: 1px solid #222;
    }
  }
  .gift_item-{
    &img{
      position: relative;
      left: 50%;
      -webkit-transform: translateX(-50%);
      transform: translateX(-50%);
      width: 5.5439rem;
      height: 4.0175rem;
      margin: .5263rem 0 .7895rem;
    }
    &main{
      text-align: center;
    }
    &title{
      line-height: 1.4;
      font-size: .2807rem;
      color: #222;
      text-overflow:ellipsis;
      white-space:nowrap;
      word-wrap: normal;
      overflow:hidden;
    }
    &parameter{
      line-height: 1.4;
      margin-top: .193rem;
      font-size: .2456rem;
      color: #9c9c9c;
      text-overflow:ellipsis;
      white-space:nowrap;
      word-wrap: normal;
      overflow:hidden;
    }
    &price--market{
      font-size: .2807rem;
      color: #9c9c9c;      
      span{
        display: inline-block;
        line-height: 16px;
        width: 36px;
        margin-top: .4561rem;
        margin-bottom: .3158rem;
        margin-right: 8px;
        font-size: 12px;
        color: #9c9c9c;
        text-align: center;
        border: 1px solid #9c9c9c;
        border-radius: 4px;
      }
    }
    &price--discount{
      font-size: .3509rem;
      color: #f47635;
      span{
        position: relative;
        top: -2px;
        display: inline-block;
        width: 20px;
        height: 20px;
        margin-right: .2105rem;
        vertical-align: middle;
        font-size: 12px;
        color: #fff;
        background-color: #f47635;
        border-radius: 10px;
      }
    }
  }
  .gift_item--big{
    width: 60%;
    box-sizing: border-box;
    border: 1px solid #222;
    .image{
      position: relative;
      top: 2.2rem;
      width: 11.7193rem;
      height: 5.0702rem;
      background-size: 100% auto;
    }
    .main{
      right: 2.2316rem;
      width: 5rem;
    }
    .title{
      font-size: .5964rem;
      font-weight: 500;
      color: #222;
    }
    .price--market{
      line-height: 1.4;
      margin: .4035rem 0 .7018rem;
      font-size: .5263rem;
      font-weight: 300;
      color: #222;
    }
    .price--discount{
      line-height: 1.4;
      margin-bottom: .6667rem;
      font-size: .5263rem;
      color: #f47635;
      span{
        position: relative;
        top: -2px;
        display: inline-block;
        width: .5614rem;
        height: .5614rem;
        margin-right: .2105rem;
        vertical-align: middle;
        font-size: .3509rem;
        color: #fff;
        text-align: center;
        background-color: #f47635;
        border-radius: 50%;
      }
    }
    .link{
      width: 1.8947rem;
      height: .8421rem;
      line-height: .8421rem;
      font-size: .3158rem;
      color: #8c8a89;
      border: 1px solid #8c8a89;
      border-radius: 4px
    }
  }
  @media (max-width: 1100px) {
    .gift_item-img{
       margin: .2rem 0;
    }
  }
  
</style>
<style>
  /* 定制tabs */
  .el-tabs__nav-scroll{
    background-color: #282828;
  }
  .el-tabs__nav{
    display: flex;
    left: 50%;
    -webkit-transform: translateX(-50%) !important;
    transform: translateX(-50%) !important;
    height: 2.0702rem;
    align-items: center;
  }
  .el-tabs--border-card>.el-tabs__header{
    border: none;
  }
  .el-tabs--top.el-tabs--border-card .el-tabs__item:nth-child(2),
  .el-tabs--top.el-tabs--border-card .el-tabs__item:last-child{
    padding: 0;
  }
  .el-tabs--border-card>.el-tabs__header .el-tabs__item{
    width: 2.8772rem;
    height: 2.0702rem;
    line-height: 2.0702rem;
    padding: 0;
    margin-top: 1px;
    font-size: .3158rem;
    text-align: center;
    color: #fff;
    border: none;
  }
  .el-tabs--border-card>.el-tabs__header .el-tabs__item:hover{
    color: #fff;
  }
  .el-tabs--border-card>.el-tabs__header .el-tabs__item.is-active{
    color: #222;
  }
  .el-tabs--border-card>.el-tabs__content{
    height: 16.4912rem;
    padding: 0;
  }
</style>

