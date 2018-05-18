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
                        key:'op_type',
                        width:100
                    },                   
                    {
                        title: '金额',
                        key: 'money', 
                        width:100                      
                    },
                     {
                        title:'类型',
                        key:'re_type',
                        width:100
                    },
                    {
                        title: '备注',
                        key: 'remark',
                       
                        
                    },
                    {
                        title: '操作人员',
                        key: 'change_people',
                        width:150
                    },
                   {
                       title:"时间",
                       key:"datetime",
                       width:150
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
            axios.get([g.http,'/finance/financerecords/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
        },
       methods:{
           updateTable(){
               axios.get([g.http,'/finance/financerecords/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
           }
           ,
           pageGetPage(page){
               axios.get([g.http,'/finance/financerecords/get','?page=',page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                    
                        });
                this.$emit("changeSider","allFinance",page);
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
