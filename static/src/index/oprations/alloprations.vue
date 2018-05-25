<template>

    <Row>
        <Col offset='4'>
            <Table border height="600" class="demo-table-info-row blue-theader" :columns="columns1" :data="data1">
                <div slot="footer">
                    <template>
                        <Row type="flex" justify="center">
                            <Col>
                                <footpage :pageinfo="pageinfo" @pageGetPage="pageGetPage"></footpage>
                            </Col>
                        </Row>
                    </template>
                </div>
            </Table>
        </Col>
    </Row>
</template>
<script>
import axios from 'axios';
import qs from 'qs';
import footpage from '../storehouse/footpage.vue';
import g from '../../libs/global.js';
import u from '../../libs/util.js';


var min_num = 60;
var max_num = 80;
 export default {
        components:{footpage},
        props:['Page','pid'],
        data () {                        
            return {                
                columns1: [
                    {
                        title:'操作',
                        key:'opration',
                        width:100
                    },
                    {
                        title: '商品名字',
                        key: 'name', 
                        width:100                      
                    },
                    {
                        title: '交易对象',
                        key: 'partner', 
                        width:100                      
                    },
                    {
                        title: '进/售价',
                        key: 'price',
                        width:max_num,
                        
                    },
                    {
                        title: '数量',
                        key: 'count',
                        width:max_num,
                    },
                    {
                        title: '总金额',
                        key: 'totalprice'
                    },
                   {
                       title:"时间",
                       key:"datetime",
                   }
                ],
                data1:[],
                pageinfo:{},
                modal_show:false,
                inputdata:[],
                
                // userid:this.changeUserId,
            }
        },
        created(){           
            axios.get([g.http,'/goods/goodschanges/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
        },
       methods:{
           updateTable(){
               axios.get([g.http,'/goods/goodschanges/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                          
                        });
           }
           ,
           pageGetPage(page){
               axios.get([g.http,'/goods/goodschanges/get','?page=',page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                    
                        });
                this.$emit("changeSider","allOprations",page);
           }
       }
    }
    
</script>
<style>
.ivu-table div.ivu-table-cell{
    text-align: center;
}
.ivu-table .demo-table-info-row td{
        background-color: #2db7f5;
        color: #fff;
    }
.ivu-table-header table thead tr th  {
    background-color: #2db7f5;
        color: #fff;
        height: 40px; 
        text-align: center;       
}
</style>
