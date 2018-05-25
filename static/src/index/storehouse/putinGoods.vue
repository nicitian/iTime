<template>
    <div>
        <br>
        <br>
        <Row class="fixedinfo">
            <Col span="5" offse="1" order="1">商品名字: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.name}}</Col>
        </Row>
        <br>        
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">进价: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.costprice}}</Col>
        </Row>
        <br>
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">售价: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.saleprice}}</Col>
        </Row>                
        <br>
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">库存: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.initotal}}</Col>
        </Row>        
        <br>
         <Row type="flex" align="middle" class="fixedinfo">
            <Col span='5' offse="1" order="1" class="success">交易对象:</Col>
            <Col span="12" offset="2" order="2">
                            <Select 
                                v-model="partner"                                
                                filterable
                                remote
                                @on-change="select"
                                :remote-method="partnerRemote"
                                :loading="partnerLoading"
                                placeholder="请输入伙伴名并选择"
                                >
                                <Option v-for="item in partners" :value="item.id" :key="item.id">{{item.value}}</Option>            
                            </Select>
            </Col>            
        </Row> 
        <br>
        <Row type="flex" align="middle" class="fixedinfo">
            <Col span='5' offse="1" order="1" class="success">入库数量:</Col>
            <Col span="6" offset="2" order="2">
                <InputNumber :min='0'  v-model="count" autofocus @on-change="input"></InputNumber >
            </Col>            
        </Row> 
        
        
    </div>
</template>
<script>
    import axios from 'axios';
    import qs from 'qs';
    import u from '../../libs/util.js';  
    import g from  '../../libs/global.js';    
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    export default {
        props:['rowdata','color'],
        data(){
            return {
                count:0,
                partner:'',
                partners:[],
                partnerLoading:false
            }
        },
        create(){
            console.log("createt call");
        },
        methods:{
             partnerRemote(query){
                 if (query != '') {
                    this.partnerLoading = true;
                    setTimeout(() => {
                        
                        axios.get([g.http,'/partner/query',"?name=",query].join('')).then(
                                                    (res)=>{
                                                        console.log(res);
                                                        this.partnerLoading = false;
                                                       this.partners = res.data;
                        });
                    }, 200);
                } else {
                    this.partners = [];
                }
            },
                select(partner){
                    this.$emit('select',partner)
                },
                input(num){
                              this.$emit('input',num);
                        }
        }
       
    }
</script>
<style scoped>
.fixedinfo div:first-of-type{
    text-align: right;
    font-weight: bold;
}
.fixedinfo div li{
    text-align: left
}
.fixedinfo div{
    font-size-adjust: inherit;    
}
.success{
    color:#2d8cf0;
}
</style>
