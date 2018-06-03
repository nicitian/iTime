<template>

    <Row >
        <Col 
        :xs="{offset:0}"
        :sm="{offset:0}"
        :md="{offset:4}"
        :lg="{offset:4}"
        >
            <Table border :height="heightView" class="demo-table-info-row blue-theader" :style="tableStyle" :columns="columns1" :data="data1">
                <div slot="footer">
                    <template>
                        <Row type="flex" justify="center">
                            <Col>
                                <footpage :pageinfo="pageinfo" @pageGetPage="pageGetPage" :isMobile="isMobile"></footpage>
                            </Col>
                        </Row>
                        <Row>

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
        props:['goodsPage','pid','isMobile'],
        data () {                        
            return {      
                       
                columnsL: [
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
                columnsS:[
                    {
                        title: '商品名字',
                        key: 'name', 
                        width:90  ,
                        fixed:'left'                    
                    },
                    
                    {
                        title: '进价',
                        key: 'costprice',
                        width:100,
                    },
                    {
                        title: '售价',
                        key: 'saleprice',
                        width:100,                   
                    },
                    {
                        title: '库存',
                        key: 'initotal',
                        width:100,
                    },
                    {
                        title: '描述',
                        key: 'desc',
                        width:139
                    },
            
                   
                    {
                        title: '操作',
                        key: 'action',
                        width: 80,
                        fixed:'right',
                        align: 'center',
                        render: this.renderButton
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
            tableStyle:function(){
                return this.isMobile ? {}:{};
            },
            heightView(){
                let height = window.innerHeight - 60;
                return this.isMobile? height:600;
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
           renderButton(h,params){

                            let opButtonL =  h('div', [
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
                             let opButtonS =  h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        margin: '5px 0px 10px 0px'
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
                                     style: {
                                        margin: '0px 0px 5px 0px'
                                    },
                                    on: {
                                        click: () => {
                                                    this.putoutGoods(params.row);
                                        }
                                    }
                                }, '出库')
                            ]);
                            return this.isMobile?opButtonS:opButtonL;
           },
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
