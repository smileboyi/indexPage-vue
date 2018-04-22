<template>
  <div>
    <div class="gift_group flex">
      <div class="gift_item--big pre">
        <i class="icon image dib2" :style="'background-image:url('+ bigGift.pic_url + ')'"></i>
        <div class="main tc dib pab hauto2">
          <h4 class="title">{{ bigGift.title }}</h4>
          <div class="price--market">
            <span>市值</span>￥{{ bigGift.market_price }}元
          </div>
          <div class="price--discount">
            <span>优</span>{{ bigGift.discount_price }}元
          </div>
          <!-- 这里没写成路由的形式，直接写的地址 -->
          <a class="link db tc wauto" :href="'/gift/'+bigGift.id">去兑换</a>
        </div>
      </div>
      <div 
        class="fe gift_item" 
        v-for="(item,index) in gifts"
        v-if="index<=1"
        :key="index"
      >
        <img class="gift_item-img" v-lazy="item.pic_url+'?'+index" alt="">
        <div class="gift_item-main">
          <a :href="'/gift/'+item.id">
            <h4 class="gift_item-title">{{ item.title }}</h4>
            <p class="gift_item-parameter">{{ item.parameter }}</p>
          </a>
          <div class="gift_item-price--market">
            <span>市值</span>￥{{ item.market_price }}元
          </div>
          <div class="gift_item-price--discount">
            <span>优</span>{{ item.discount_price }}元
          </div>
        </div>
      </div>
    </div>
    <div class="gift_group flex">
      <div 
        class="fe gift_item" 
        v-for="(item,index) in gifts"
        v-if="index>1"
        :key="index"
      >
        <img class="gift_item-img" v-lazy="item.pic_url+'?'+index">
        <div class="gift_item-main">
          <a :href="'/gift/'+item.id">
            <h4 class="gift_item-title">{{ item.title }}</h4>
            <p class="gift_item-parameter">{{ item.parameter }}</p>
          </a>
          <div class="gift_item-price--market">
            <span>市值</span>￥{{ item.market_price }}元
          </div>
          <div class="gift_item-price--discount">
            <span>优</span>{{ item.discount_price }}元
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {  
    bigGift: {  
      type: Object,  
      required: true  
    },  
    gifts: {
      type: Array,  
      required: true  
    }  
  },
}
</script>

<style lang="less" scoped>

</style>
