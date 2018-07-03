<template>
    <Layout>
        <Row v-if="isMobile === false" >
            <Col offset="4">
                <Row type="flex" justify="space-between">
                    <Col span='5'>
                        <DatePicker @on-change="changeStartdate" v-model="startdate" transfer type="date" format="yyyy-MM-dd"  placeholder="开始日期" style="width: 200px"></DatePicker>
                    </Col>
                    <Col span='5'>
                        <DatePicker @on-change="changeEnddate" v-model="enddate" transfer  type="date"  format="yyyy-MM-dd" placeholder="结束日期" style="width: 200px"></DatePicker>
                    </Col>
                    <Col span='3'>                        
                        <Select v-model="opt"  placeholder="操作">
                                <Option v-for="item in opts" :value="item.value" :key="item.value">{{item.label}}</Option>            
                        </Select>
                    </Col>
                    <Col span='3'>                        
                        <Select v-model="type"  placeholder="类型">
                                <Option v-for="item in types" :value="item.value" :key="item.value">{{item.label}}</Option>            
                        </Select>
                    </Col>
                    <Col span='2'>
                        <Button type="primary" @click="handleQuery()">查询</Button>
                    </Col>
                </Row>
            </Col>
        </Row>
        <Row :style="{height:heightView+'px'}">
            <Col 
                :xs="{offset:0}"
                :sm="{offset:0}"
                :md="{offset:4}"
                :lg="{offset:4}">
                <Row v-if="isMobile" type="flex">
                    <Col span="12" >
                        <DatePicker @on-change="changeStartdate" v-model="startdate" transfer type="date" format="yyyy-MM-dd"  placeholder="开始日期" ></DatePicker>
                    </Col>
                    <Col span="12">
                        <DatePicker @on-change="changeEnddate" v-model="enddate" transfer  type="date"  format="yyyy-MM-dd" placeholder="结束日期" ></DatePicker>
                    </Col>
                </Row>
                <Row v-if="isMobile" type="flex">
                   
                    <Col span="12">                                                
                        <Select v-model="opt"  placeholder="操作">
                                <Option v-for="item in opts" :value="item.value" :key="item.value">{{item.label}}</Option>            
                        </Select>
                    </Col>
                    
                    <Col span="12">                                                
                        <Select v-model="type"  placeholder="类型">
                                <Option v-for="item in types" :value="item.value" :key="item.value">{{item.label}}</Option>            
                        </Select>
                    </Col>
                </Row>
                <Row v-if="isMobile" type="flex" justify="space-between">
                    <Col span="24">
                        <Button type="primary" @click="handleQuery()">查询</Button>
                    </Col>
                </Row>
                <Row >
                    <Col>
                        <Table border  class="demo-table-info-row blue-theader" :columns="columns1" :data="data1">                            
                            <div slot="footer" style="{height:300px}"> 
                                <template>                            
                                    <Row v-if="isMobile === false" type="flex" justify="space-between">
                                        <Col push='1'> 
                                            <Row class="footer-text" type="flex" justify="space-between" :gutter="16">   
                                                <Col>                                                    
                                                    <p>总资金：{{total.finance}} </p>
                                                </Col>
                                                <Col>
                                                    <p>总收入:{{total.income}}</p>
                                                </Col>
                                                <Col >
                                                    <p>总支出：{{total.cost}}</p>
                                                </Col>
                                            </Row>                            
                                        </Col>
                                        <Col pull='1'>
                                            <footpage :pageinfo="pageinfo" @pageGetPage="pageGetPage"></footpage>
                                        </Col>                                
                                    </Row>                                                                                                                                        

                                    <Row v-if="isMobile" type="flex" justify="center">
                                        <Col>
                                            <footpage :pageinfo="pageinfo" @pageGetPage="pageGetPage"></footpage>
                                        </Col>
                                    </Row>

                                </template>                                     
                            </div>     
                        </Table>
                    </Col>
                </Row>
                <Row v-if="isMobile" type="flex" justify="center">
                    <Col span='6'>
                        <Row type="flex" justify=center>
                            <label> 总资金</label>                         
                            <InputNumber 
                            v-model="total.finance" 
                            readonly                         
                            :formatter="value => `￥ ${value}`.replace(/B(?=(d{3})+(?!d))/g, ',')"
                            :parser="value => value.replace(/$s?|(,*)/g, '')"></InputNumber>
                        </Row>
                    </Col>
                    <Col span='6'>
                        
                        <Row type="flex" justify=center>
                            <label> 总收入</label>                         
                            <InputNumber 
                            v-model="total.income" 
                            readonly                         
                            :formatter="value => `￥ ${value}`.replace(/B(?=(d{3})+(?!d))/g, ',')"
                            :parser="value => value.replace(/$s?|(,*)/g, '')"></InputNumber>
                        </Row>
                    </Col>
                    <Col span='6'>                        
                        <Row type="flex" justify=center>
                            <label> 总支出：</label>                         
                            <InputNumber 
                            v-model="total.cost" 
                            readonly                         
                            :formatter="value => `￥ ${value}`.replace(/B(?=(d{3})+(?!d))/g, ',')"
                            :parser="value => value.replace(/$s?|(,*)/g, '')"></InputNumber>
                        </Row>
                    </Col>

                </Row>
            </Col>
        </Row>
    </Layout>
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
                        title:'操作',
                        key:'op_type',
                        width:100
                    },
                    {
                        title:'交易对象',
                        key:'partner',
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
                columnsS: [
                    {
                        title:'操作',
                        key:'op_type',
                        width:80,
                        fixed:'left'
                    },     
                    {
                        title:'交易对象',
                        key:'partner',
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
                        width:200                                           
                    },
                    {
                        title: '操作人员',
                        key: 'change_people',
                        width:150
                    },
                   {
                       title:"时间",
                       key:"datetime",
                       width:200
                   }
                ],
                frURL:'/finance/financerecords/get',
                querystring:'',
                data1:[],
                startdate:'',
                enddate:'',
                type:'所有',
                opt:'所有',
                total:{
                        finance:0,
                        income:0,
                        cost:0
                },
                    opts: [
                        {
                            value:'收入',
                            label:'收入',
                        },
                        {
                            value:'支出',
                            label:'支出'
                        },
                        {
                            value:'所有',
                            label:'所有'
                        }
                    ],   
                    types:[
                            {
                                value:'入库',
                                label:'入库'
                            },
                            {
                                value:'出库',
                                label:'出库'
                            },
                            {
                                value:'其他',
                                label:'其他'
                            },
                            {
                                value:'所有',
                                label:'所有'
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
            columns1(){
                return this.isMobile ? this.columnsS:this.columnsL;
            },     
            widthView(){
                let width = window.innerWidth
                return {width:width+"px"}
            }   ,  
            heightView(){
                let height = window.innerHeight - 60;
                return this.isMobile? height:600;
            }
        },
        created(){    
            let getURL =  [g.http,'/finance/financerecords/get',"?page=",this.Page].join('')      
            axios.get(getURL).then(
                                    (res)=>{
                                        this.data1=res.data.body;   
                                        this.pageinfo=res.data.pageinfo;                                                          
                        });
            axios.get([g.http,'/finance/get'].join('')).then(
                                                    (res)=>{
                                                       this.total=res.data.body;  
                                                                                                                                                                
                        });         
            u.dateini();
        },
       methods:{
           changeOpt(val){
               

           },
           changetype(val){

           },
           changeStartdate(fmt,dat){               
               this.startdate= fmt;
               
           },
           changeEnddate(fmt,date){               
               this.enddate = fmt               
           },
           handleQuery(){
               let fmt = this.enddate

               u.dateini();
               let sdate;
               if(fmt=='')
                     sdate = new Date("2100-01-01"); 
                else
                     sdate = new Date(fmt);
               sdate.addDays(1);               
               let enddate = sdate.Format("yyyy-MM-dd");               
               console.log(this.enddate);

               this.querystring = [
                                "&startdate=",this.startdate,
                                "&enddate=",enddate,
                                "&type=",this.type,
                                "&opt=",this.opt,
                                "&isquery=",true].join('')
                                
               let frURL =  [g.http,'/finance/financerecords/get',"?page=",this.Page,this.querystring].join('') 
                axios.get(frURL).then(
                                    (res)=>{
                                        this.data1=res.data.body;   
                                        this.pageinfo=res.data.pageinfo;                                                          
                        });                        
               console.log("开始：",this.startdate,"结束",this.enddate.toString(),"类型：",this.type,"操作：",this.opt);
               let start_date;
               let end_date;
                if(this.startdate=='')
                     start_date = new Date("2018-01-01");
                else
                     start_date = new Date(this.startdate);
                let change_start_date = start_date;
                if(this.enddate=='')
                     end_date = new Date("2100-01-01");
                else
                     end_date = new Date(enddate);
                end_date.addDays(1);
                let change_end_date = end_date;

                let start_year_month = start_date.getFullYear()*100+start_date.getMonth()+1;
                let str_start_date_gte = start_date.Format("yyyy-MM-dd");
                change_start_date.addMonths(1);
                change_start_date.setDate(1);
                let str_start_date_lt = change_start_date.Format("yyyy-MM-dd");

                let end_year_month = end_date.getFullYear()*100+end_date.getMonth()+1;
                let str_end_date_lte = end_date.Format("yyyy-MM-dd");
                change_end_date.setDate(1);
                let str_end_date_gte = change_end_date.Format("yyyy-MM-dd");

                let queryfi = ["?type=",this.type,
                                "&opt=",this.opt,
                                "&str_start_date_gte=",str_start_date_gte,
                                "&str_start_date_lt=",str_start_date_lt,

                                "&start_year_month=",start_year_month,
                                "&end_year_month=",end_year_month,

                                "&str_end_date_gte=",str_end_date_gte,
                                "&str_end_date_lte=",enddate,
                                "&isquery=",true
                                ].join('')

                let fiURL =  [g.http,'/finance/get',queryfi].join('') ;
                axios.get(fiURL).then(
                                    (res)=>{
                                        this.total=res.data.body;                                                                                                 
                                    });

           },
           updateTable(){
               axios.get([g.http,'/finance/financerecords/get',"?page=",this.Page].join('')).then(
                                                    (res)=>{
                                                            this.data1=res.data.body;   
                                                            this.pageinfo=res.data.pageinfo;                                                          
                        });
           }
           ,
           pageGetPage(page){
               console.log([this.frURL,"?page=",page,this.querystring]);   

               axios.get([this.frURL,"?page=",page,this.querystring].join('')).then(
                                                    (res)=>{
                                                       this.data1=res.data.body;   
                                                       this.pageinfo=res.data.pageinfo;                                                    
                        });
                this.$emit("changeSider","queryFinance",page);
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
.ivu-table-header table thead tr th{
    background-color: #2db7f5;
    color: #fff;
    height: 40px; 
    text-align: center;       
}
.footer-text Col p{
    font-size-adjust: inherit;
    color:#2db7f5;
}
</style>
