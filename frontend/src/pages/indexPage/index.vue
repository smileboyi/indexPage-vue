<template>
  <div>
    <pageTop />
    <!-- <pageBottom /> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import pageBottom from '@/components/pageBottom'
import pageTop from './pageTop'


export default {
  computed: {
    ...mapState([
    ]),
  },
  components:{
    pageTop,
    pageBottom
  }
}
</script>

<style lang="less" scoped>

</style>
