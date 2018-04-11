export default {
  namespaced: true,
  state: {  
    isViedoPlay: false,
    viedoSrc: "",
  },  
  mutations: {  
    playVideo(state,data){
      state.isViedoPlay = true;
      state.viedoSrc = data.src;
    },
    closeVideo(state,data){
      state.isViedoPlay = false;
    },
  },
  actions: {

  }
}