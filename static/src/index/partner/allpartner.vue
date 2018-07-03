<template>

    <Row>
        <Col 
            :sm="{offset:0}"
            :md="{offset:4}"
            >
            <Table border :height="heightView" class="demo-table-info-row blue-theader" :columns="columns1" :data="data1">
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
        props:['Page','pid','isMobile'],
        data () {                        
            return {                
                columnsL: [
                    {
                        title:'名字',
                        key:'name',
                        width:100
                    },
                    {
                        title: '合作关系',
                        key: 'relative', 
                        width:100                      
                    },
                    {
                        title: '商品',
                        key: 'goods',
                        
                        
                    },
                    {
                        title: '负责人',
                        key: 'charge_person',
                        width:max_num,
                    },
                    {
                        title: '联系方式',
                        key: 'phone_number'
                    },
                   {
                       title:"地址",
                       key:"address",
                   }
                   ,
                   {
                       title:"备注",
                       key:"remark",
                   }
                ],
                 columnsS: [
                    {
                        title:'名字',
                        key:'name',
                        fixed:'left',
                        width:100
                    },
                    {
                        title: '合作关系',
                        key: 'relative', 
                        width:100                      
                    },
                    {
                        title: '商品',
                        key: 'goods',
                        width:100     
                        
                    },
                    {
                        title: '负责人',
                        key: 'charge_person',
                        width:100  ,
                    },
                    {
                        title: '联系方式',
                        key: 'phone_number',
                        width:150
                    },
                   {
                       title:"地址",
                       key:"address",
                       width:200
                   }
                   ,
                   {
                       title:"备注",
                       key:"remark",
                       width:200
                   }
                ],
                data1:[],
                pageinfo:{},
                modal_show:false,
                inputdata:[],
                
                // userid:this.changeUserId,
            }
        },
        computed:{
            columns1:function(){
                return this.isMobile?this.columnsS:this.columnsL;
            },
            rowStyle(){
                return this.isMobile ? {
                    height:[this.rowHight,'px'].join(''), 
                    paddingTop:"100px"                   
                }:{}
            },
            heightView(){
                let height = window.innerHeight - 60;
                return this.isMobile? height:600;
            }
        },
        created(){           
            axios.get([g.http,'/partner/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
        },
       methods:{
           updateTable(){
               axios.get([g.http,'/partner/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
           }
           ,
           pageGetPage(page){
               axios.get([g.http,'/partner/get','?page=',page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                    
                        });
                this.$emit("changeSider","allPartner",page);
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
