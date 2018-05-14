<template>
  <Page :current="pageinfo.current" :total="pageinfo.total" show-elevator show-total :page-size="pageinfo.size"  @on-change="getPage"></Page>
</template>
<script>
export default {
  props:["pageinfo"],
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
