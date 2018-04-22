<template>
  <section class="grail">
    <page-top/>
    <feature-box/>
    <resume-box/>
    <hr-box :hrDatas="hrDatas"/>
    <gift-box/>
  </section>
</template>

<script>
import hrBox from '~/components/home/hrBox.vue'
import pageTop from '~/components/home/pageTop.vue'
import giftBox from '~/components/home/giftBox.vue'
import resumeBox from '~/components/home/resumeBox.vue'
import featureBox from '~/components/home/featureBox.vue'
import { getHrDatas } from '~/api/api';


export default {
  async asyncData ({ params }) {
    let { data } = await getHrDatas({});
    return { hrDatas:data }
  },
  components: {
    hrBox,
    pageTop,
    giftBox,
    resumeBox,
    featureBox
  }
}
</script>

<style>

</style>
