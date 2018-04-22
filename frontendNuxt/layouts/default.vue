<template>
  <div class="grail w100">
    <nuxt/>
    <page-bottom/>
  </div>
</template>
<script>
import pageBottom from '~/components/common/pageBottom.vue'


export default {
  components: {
    pageBottom
  }
}
</script>
<style>
  /* 除了在config中配置，也可以在style中引入 */
  @import url("~/assets/css/wl.base.css");
  body{
    max-width: 1900px;
    min-width: 900px;
  }
</style>

