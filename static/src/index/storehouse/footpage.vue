<template>
  <Page :current="pageinfo.current" :total="pageinfo.total" :show-elevator="!isMobile" show-total :page-size="pageinfo.size"  @on-change="getPage"></Page>
</template>
<script>
export default {
  props:["pageinfo","isMobile"],
  data(){
      return {
          data:[]
      }
  },
  methods:{
      getPage(page){
          console.log("call getpage",page)
          this.$emit("pageGetPage",page);
      }
  }
}
</script>
