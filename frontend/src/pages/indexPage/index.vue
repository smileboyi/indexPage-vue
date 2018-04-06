<template>
  <div>
    <pageTop />
    <featureBox />
    <resumeBox />
    <hrBox />
    <giftBox />
    <pageBottom />
  </div>
</template>

<script>
import pageBottom from '@/components/pageBottom'
import pageTop from './pageTop'
import featureBox from './featureBox'
import resumeBox from './resumeBox'
import hrBox from './hrBox'
import giftBox from './giftBox'


export default {
  components:{
    pageTop,
    featureBox,
    resumeBox,
    hrBox,
    giftBox,
    pageBottom
  }
}
</script>

<style lang="less" scoped>

</style>
