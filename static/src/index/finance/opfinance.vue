<template>
    <Row>
        <Col span="12" offset="4">
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">

                <FormItem label="操作类型" prop="type">
                    <!-- <Input v-model="formValidate.initotal" placeholder="请填入初始库存"></Input> -->
                    <Select v-model="formValidate.type" style="width:80px">
                        <Option v-for="item in formValidate.types" :value="item.value" :key="item.value">{{item.label}}</Option>            
                    </Select>
                </FormItem>
                <Row>
                    <Col span="4">
                        <FormItem label="交易对象"  prop="partner">                        
                            <Select 
                                v-model="formValidate.partner"                                
                                filterable
                                remote
                                :remote-method="partnerRemote"
                                :loading="formValidate.partnerLoading"
                                placeholder="请输入伙伴名并选择"
                                style="width:220px">
                                <Option v-for="item in formValidate.partners" :value="item.id" :key="item.id">{{item.value}}</Option>            
                            </Select>
                        </FormItem>
                    </Col>
                </Row>
                <FormItem label="金额" prop="finance">
                    <!-- <Inputnumber v-model="formValidate.costprice" placeholder="请填入产品进价"></Input> -->
                    <Input-number   v-model="formValidate.finance" placeholder="请填入总资金"></Input-number>
                </FormItem>
                
                <FormItem label="修改原因" prop="reason">
                    <Input v-model="formValidate.reason" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入修改财务的理由"></Input>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
                    <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
                </FormItem>
            </Form>
        </Col>
    </Row>
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
        props:['pid'],
        data () {
            return {
                formValidate: {
                    types: [
                        {
                            value:'收入',
                            label:'收入',
                        },
                        {
                            value:'支出',
                            label:'支出'
                        }
                    ],
                    type:'',
                    finance:0,//金额
                    reason: '',
                    partner:'',
                    partnerLoading:false,
                    partners:[]
                },
                ruleValidate: {       
                    finance:[                        
                        {type:'number',message:'只能输入数字'}
                    ],
                    type:[
                        {type:'string',required:true,message:'操作类型为必填项'}
                    ],
                
                    reason: [
                        { required: true, message: '请输入操作财务的理由', trigger: 'blur' },
                        { type: 'string', message: '描述不能少于20个字符', trigger: 'blur' }
                    ]
                }

            }
        },
        methods: {
            partnerRemote(query){
                 if (query != '') {
                    this.formValidate.partnerLoading = true;
                    setTimeout(() => {
                        
                        axios.get([g.http,'/partner/query',"?name=",query].join('')).then(
                                                    (res)=>{
                                                        console.log(res);
                                                        this.formValidate.partnerLoading = false;
                                                       this.formValidate.partners = res.data;
                        });
                    }, 200);
                } else {
                    this.formValidate.partners = [];
                }
            },
            handleSubmit (name) {                
                this.$refs[name].validate((valid) => {
                    if (valid) {
                                var data = {
                                            
                                            type:this.formValidate.type,                                            
                                            finance:this.formValidate.finance,
                                            reason:this.formValidate.reason,
                                            userid:this.pid,
                                            partner:this.formValidate.partner                                       
                                        };

                                data = qs.stringify(data);

                                axios.post(
                                            "/finance/edit",
                                             data,
                                             {
                                                headers:{
                                                         'Content-Type':'application/x-www-form-urlencoded',                            
                                                         },
                                             }
                                        ).then(
                                                res =>{
                                                        if(u.ajaxCallBack(res,'操作成功！',this.$Message))
                                                            this.$emit('changeSider','allFinance');
                                                }
                                            );
                        
                    } else {
                        this.$Message.error('填写有误!');
                    }
                })
            },
            handleReset (name) {
                this.$refs[name].resetFields();
            }
        }
    }
</script>
