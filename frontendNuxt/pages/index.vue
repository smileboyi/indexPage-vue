<template>
  <section class="container">
    <!-- <app-logo/> -->
    <page-top/>
    <feature-box/>
    <resume-box/>
  </section>
</template>

<script>
// import AppLogo from '~/components/AppLogo.vue'
// import hrBox from '~/components/home/hrBox.vue'
import pageTop from '~/components/home/pageTop.vue'
// import giftBox from '~/components/home/giftBox.vue'
import resumeBox from '~/components/home/resumeBox.vue'
import featureBox from '~/components/home/featureBox.vue'


export default {
  components: {
    pageTop,
    resumeBox,
    featureBox
  }
}
</script>

<style>
/* .container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
} */
</style>
