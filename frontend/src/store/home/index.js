export default {
  namespaced: true,
  state: {  
    isViedoPlay: false
  },  
  mutations: {  
    switchViedoPlay: function(state,data){
      state.isViedoPlay = data.isViedoPlay;
    }
  },
  actions: {

  }
}