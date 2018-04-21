export default {
  namespaced: true,
  state: {  
    isViedoPlay: false,
    viedoSrc: "",
  },  
  mutations: {
    // 播放前传入src
    conveyVideoSrc(state, data){
      state.viedoSrc = data.src;
    },
    // 打开或关闭
    switchVideoState(state,data) {
      state.isViedoPlay = data.play;
    }
  },
  actions: {

  }
}