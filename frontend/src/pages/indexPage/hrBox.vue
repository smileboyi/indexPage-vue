<template>
  <div class="hr">
    <h2 class="hr_title tc">
      <span class="cor2">1000+</span>
      HR精英智慧之选
    </h2>
    <p class="hr_text tc">
      简历已下载
      <span class="cor2">16900次</span>
    </p>
    <div class="hr_main pre" @mouseout="handleMouseOut()">
      <div class="flex hr_list h50">
        <div 
          class="icon hr_item fe" 
          v-for="(item,index) in hrDatas" 
          v-if="index<=5"
          :style="'background-image:url('+ item.pic_url + ')'"
          @mouseover="handleMouseOver(index,item.details)"
          :key="index"
        >
          <a 
            class="hr_item-play" 
            href="javascript:;"
            v-if="item.viedeo_src!=''"
            @click="handleVideoPlay(item.viedeo_src)"
          >
            <img src="../../assets/img/play-btn.png" />
          </a>
        </div>
      </div>

      <div class="flex hr_list h50">
        <div 
          class="icon hr_item fe" 
          v-for="(item,index) in hrDatas" 
          v-if="index>5"
          :style="'background-image:url('+ item.pic_url + ')'"
          @mouseover="handleMouseOver(index,item.details)"
          :key="index"
        >
          <a 
            class="hr_item-play" 
            href="javascript:;"
            v-if="item.viedeo_src!=''"
            @click="handleVideoPlay(item.viedeo_src)"
          >
            <img src="../../assets/img/play-btn.png" />
          </a>
        </div>
      </div>

      <div class="hr_show pab h50" :style="positionObj" v-show="isShow">
        <span class="hr_show-year pab test-spaced tc">{{hrDetails.join_year}}年加入</span>
        <div class="hr_show-info pre">
          <a class="hr_show-share dib tc pab" :href="'/hr/'+hrDetails.id+'share'">分享</a>
          <div class="hr_show-right">
            <p class="hr_show-name">{{hrDetails.name}}（{{hrDetails.sex}}）</p>
            <p class="hr_show-text">{{hrDetails.text}}</p>
          </div>
        </div>
        <div class="flex hr_show-data">
          <div class="hr_show-item">
            下载简历：<span class="hr_show-num">{{hrDetails.download_num}}份</span>
          </div>
          <div class="hr_show-item">
            分享简历：<span class="hr_show-num">{{hrDetails.share_num}}份</span>
          </div>
          <div class="hr_show-item">
            兑换礼品：<span class="hr_show-num">{{hrDetails.convert_num}}份</span>
          </div>
          <div class="hr_show-item">
            礼品价值：<span class="hr_show-num">￥{{hrDetails.gift_value}}元</span>
          </div>
        </div>
      </div>
      <videoPlayer />
    </div>
  </div>
</template>

<script>
  import { mapMutations } from 'vuex'
  import { getHrDatas } from '@/api/api';
  import videoPlayer from '@/components/videoPlayer'


  export default {
    data(){
      return {
        isShow: false,
        hrDatas: [],
        positionObj:{
          left: "0%",
          top: "0%"
        },
        hrDetails: {
          name: "",
          join_year: "",
          id: "",
          text: "",
          download_num: 0,
          share_num: 0,
          convert_num: 0,
          gift_value: 0
        }
      };
    },
    created(){
      // 实例创建后，初始化列表数据，页面还没渲染时调用init方法。
      this.init();
    },
    methods:{
      ...mapMutations('home', [
        "conveyVideoSrc",
        "switchVideoState"
      ]),
      init(){
        getHrDatas({}).then(res => {
          this.hrDatas = res.data.datas;
        });
      },
      handleMouseOver(index, details){
        if(this.isShow) return;
        if(index<6){
          if(index<4){
            this.positionObj = {
              left: 16.6666*(index+1)+"%",
              top: '0%'
            };
          }else{
            this.positionObj = {
              left: 16.6666*(index-2)+"%",
              top: '0%'
            };
          }
        }else{
          if(index<9){
            this.positionObj = {
              left: 16.6666*(index-5)+"%",
              top: '50%'
            };
          }else{
            this.positionObj = {
              left: 16.6666*(index-8)+"%",
              top: '50%'
            };
          }
        }
        this.hrDetails = details;
        this.isShow = true;
      },
      handleMouseOut(){
        this.isShow = false;
      },
      handleVideoPlay(src){
        this.conveyVideoSrc({ src:src });
        this.switchVideoState({ play:true });
      }
    },
    components:{
      videoPlayer
    }
  }
</script>

<style lang="less" scoped>
  .hr{
    padding: 1.8421rem 0 .9825rem;
    border-bottom: 2px solid #f4f4f4;
  }
  .hr_{
    &title{
      font-size: .5965rem;
      font-weight: 400;
    }
    &text{
      margin: .4737rem auto 1.6842rem;
      font-size: .4211rem;
      color: #6c6c6c;
    }
    &main{
      height: 10.5263rem;
    }
    &item{
      position: relative;
      &:hover{
        .hr_item-play{
          display: block;
        }
      }
    }
    &item-play{
      display: none;
      position: absolute;
      top: 50%;
      left: 50%;
      -webkit-transform: translate(-50%, -50%);
      transform: translate(-50%, -50%);
      width: 1.4035rem;
      height: 1.4035rem;
    }
  }
  .hr_show{
    width: 33.3333%;
    // left: 33.3333%;
    // top: 50%;
    background-color: rgba(22, 22, 22, .8);
  }
  .hr_show-{
    &year{
      top: .8772rem;
      right: .8772rem;
      line-height: .614rem;
      width: 2.1404rem;
      font-size: .3158rem;
      color: #f47635;
      border: 1px solid #f47635;
      border-radius: .307rem;
    }
    &info{
      margin-left: .9649rem;
      margin-top: 1.5263rem; 
    }
    &share{
      bottom: .1rem;
      line-height: .4561rem;
      width: 1rem;
      font-size: .2807rem;
      font-size: 12px;
      color: #fff;
      border: 1px solid #fff;
      border-radius: .2280rem;
    }
    &right{
      margin-left: 1.1579rem;
      color: #fff;
    }
    &name{
      line-height: 1.4;
      font-size: .386rem;
    }
    &text{
      line-height: 1.4;
      margin-top: .193rem;
      font-size: .2807rem;
    }
    &data{
      width: 8.5702rem;
      margin-left: .9649rem;
      margin-top: .5614rem;
      flex-wrap:wrap;
    }
    &item{
      width: 50%;
      font-size: .2807rem;
      color: #bebebe;
    }
    &num{
      color: #fff;
    }
  }
</style>
