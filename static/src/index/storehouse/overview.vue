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
import footpage from './footpage.vue';
import g from '../../libs/global.js';
import u from '../../libs/util.js';
import putin from './putinGoods.vue';
import putout from './putoutGoods.vue';
var number_width = 80;
 export default {
        components:{footpage,putin,putout},
        props:['goodsPage','pid'],
        data () {                        
            return {                
                columns1: [
                    {
                        title: '商品名字',
                        key: 'name', 
                        width:100                      
                    },
                    {
                        title: '进价',
                        key: 'costprice',
                        minWidth:number_width
                    },
                    {
                        title: '售价',
                        key: 'saleprice',
                        minWidth:number_width                        
                    },
                    {
                        title: '库存',
                        key: 'initotal',
                        minWidth:number_width
                    },
                    {
                        title: '描述',
                        key: 'desc'
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 150,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '7px'
                                    },
                                    on: {
                                        click: () => {
                                            this.putinGoods(params.row)
                                        }
                                    }
                                }, '入库'),
                                h('Button', {
                                    props: {
                                        type: 'success',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                                    this.putoutGoods(params.row);
                                        }
                                    }
                                }, '出库')
                            ]);
                        }
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
            axios.get([g.http,'/goods/get',"?page=",this.goodsPage].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
        },
       methods:{
           updateTable(){
               axios.get([g.http,'/goods/get',"?page=",this.goodsPage].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;   
                                                       

                        });
           }
           ,
           pageGetPage(page){
               axios.get([g.http,'/goods/get','?page=',page].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                    
                        });
                this.$emit("changeSider","overview",page);
           },
           putinGoods(rdata){               
               let count = 0;
               let partner = '';
               let userid = this.pid;
               let page = this.goodsPage
               let self = this.$Message
               let update = this.updateTable
               function onok(){                                       
                                let http = [g.http,'/goods/goodschanges/create','?count=',count,'&',"goodsid=",rdata.id,'&userid=',userid,'&type=','入库'].join('');  
                                let Params = {
                                    count,
                                    goodsid:rdata.id,
                                    userid,
                                    price:rdata.price,
                                    partner
                                }
                                console.log('onok····',http)        
                                axios.get([g.http,'/goods/goodschanges/create'].join(''),{params:Params}).then((res)=>{
                                    
                                    // u.ajaxCallBack(res,"入库成功",self,true,toUrl);  
                                    self.success("入库成功！") ;
                                    update();                                    
                                });
                            }

                function setCount(num){count = num;}     
                function setPartner(p_id){partner = p_id;}     
            
                let config = {
                                title:"<p style='color:#2d8cf0'>请填写商品入库数量...</p>",
                                width:350,
                                value:true,
                                okText:"入库",
                                onOk:onok,                                                       
                                render:h =>h(putin,{
                                                    props:{rowdata:rdata},
                                                    on:{input:setCount,
                                                        select:setPartner},                                                    
                                                }   
                                        )                                                                                    
                        }
                this.$Modal.confirm(config);
           },         
           putoutGoods(rdata){
               let count = 0;
               let partner = '';
               let userid = this.pid;
               let page = this.goodsPage
               let self = this.$Message
               let update = this.updateTable
               function onok(){                                       
                                let http = [g.http,'/goods/goodschanges/create','?count=',count,'&',"goodsid=",rdata.id,'&userid=',userid,'&type=出库'].join('');  
                                let Params = {
                                    count,
                                    goodsid:rdata.id,
                                    userid,
                                    price:rdata.price,
                                    type:'出库',
                                    partner
                                }
                                console.log('onok····',http)        
                                axios.get([g.http,'/goods/goodschanges/create'].join(''),{params:Params}).then((res)=>{
                                    
                                    // u.ajaxCallBack(res,"入库成功",self,true,toUrl);  
                                    self.success("出库成功！") ;
                                    update();                                    
                                });
                            }

                function setCount(num){count = num;}     
                function setPartner(p_id){partner = p_id;}     

                let config = {
                                title:"<p style='color:#19be6b'>请填写商品出库数量...</p>",
                                width:350,
                                value:true,
                                okText:"出库",
                                onOk:onok,                                                       
                                render:h =>h(putout,{
                                                    props:{rowdata:rdata},
                                                    on:{input:setCount,
                                                        select:setPartner},                                                    
                                                }   
                                        )                                                                                    
                        }
                this.$Modal.confirm(config);
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
