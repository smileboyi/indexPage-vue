<template>
  <div class="player pfi wh100 not z50" v-if="home.isViedoPlay">
    <div class="player_bg wh100" @click="switchVideoState({ play:false })"></div>
    <video-player   
      class="vjs-custom-skin w75 centre2"
      ref="videoPlayer"
      :options="playerOptions"
      :playsinline="true"
      @play="onPlayerPlay($event)"
      @pause="onPlayerPause($event)"
      @ended="onPlayerEnded($event)"
      @loadeddata="onPlayerLoadeddata($event)"
      @waiting="onPlayerWaiting($event)"
      @playing="onPlayerPlaying($event)"
      @timeupdate="onPlayerTimeupdate($event)"
      @canplay="onPlayerCanplay($event)"
      @canplaythrough="onPlayerCanplaythrough($event)"
      @ready="playerReadied"
      @statechanged="playerStateChanged($event)"
    />
  </div>
</template>
 
<script>
  import { mapState, mapMutations } from 'vuex'
  import VueVideoPlayer from 'vue-video-player'
  import 'video.js/dist/video-js.css'

  export default {
    data() {
      return {
        // videojs options
        playerOptions: {
          // height: document.documentElement.clientHeight,
          // width: document.documentElement.clientWidth,
          autoplay: true,
          muted: true,    // 默认情况下将会消除任何音频。
          language: 'zh-CN',
          playbackRates: [0.7, 1.0, 1.5, 2.0],  //播放速度
          fluid: true,    //将按比例缩放以适应其容器
          sources: [{
            type: "video/mp4",
            // mp4
            src: "http://vjs.zencdn.net/v/oceans.mp4",
          }],
          poster: "https://surmon-china.github.io/vue-quill-editor/static/images/surmon-1.jpg",   //封面地址
        }
      }
    },
    computed: {
      ...mapState(['home']),
      player() {
        return this.$refs.videoPlayer.player
      }
    },
    beforeUpdate: function(){
      this.playerOptions.sources = [{
        type: "video/mp4",
        src: this.home.viedoSrc,
      }];
    },
    methods: {
      ...mapMutations('home', [
        "switchVideoState"
      ]),
      // listen event
      onPlayerPlay(player) {
        // console.log('player play!', player)
      },
      onPlayerPause(player) {
        // console.log('player pause!', player)
      },
      onPlayerEnded(player) {
        this.switchVideoState({ play:false });
        // console.log('player ended!', player)
      },
      onPlayerLoadeddata(player) {
        // console.log('player Loadeddata!', player)
      },
      onPlayerWaiting(player) {
        // console.log('player Waiting!', player)
      },
      onPlayerPlaying(player) {
        // console.log('player Playing!', player)
      },
      onPlayerTimeupdate(player) {
        // console.log('player Timeupdate!', player.currentTime())
      },
      onPlayerCanplay(player) {
        // console.log('player Canplay!', player)
      },
      onPlayerCanplaythrough(player) {
        // console.log('player Canplaythrough!', player)
      },
      // or listen state event
      playerStateChanged(playerCurrentState) {
        // console.log('player current update state', playerCurrentState)
      },
      // player is ready
      playerReadied(player) {
        // console.log('example player 1 readied', player)
      },
    },
    components: {
      VueVideoPlayer
    }
  }
</script>
<style>
  /* 覆盖插件的默认样式，不用scoped */
  .player_bg{
    background-color: rgba(22, 22, 22, .5);
  }
  .vjs-custom-skin{
    max-width: 1200px;
  }
  .vjs-big-play-button{	
    top: 50% !important;
    left: 50% !important;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
  }
</style>

