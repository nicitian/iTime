<template>
    <Row>
        <Col span="12" offset="4">
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                
                <FormItem label="总资金" prop="finance">
                    <!-- <Inputnumber v-model="formValidate.costprice" placeholder="请填入产品进价"></Input> -->
                    <Input-number readonly  v-model="formValidate.finance" placeholder="请填入总资金"></Input-number>
                </FormItem>
                <FormItem label="总收入" prop="income">
                    <!-- <Input v-model="formValidate.saleprice" placeholder="请填入产品售价"></Input> -->
                    <Input-number  readonly type="number"  v-model="formValidate.income" placeholder="请填入总收入"></Input-number>
                </FormItem>
                <FormItem label="总支出" prop="cost">
                    <!-- <Input v-model="formValidate.initotal" placeholder="请填入初始库存"></Input> -->
                    <Input-number readonly v-model="formValidate.cost" placeholder="请填入总支出"></Input-number>
                </FormItem>
                
                <!-- <FormItem label="修改原因" prop="reason">
                    <Input v-model="formValidate.reason" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入修改财务的理由"></Input>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="handleSubmit('formValidate')">修改</Button>
                    <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
                </FormItem> -->
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
        data () {
            return {
                formValidate: {
                    name: '',
                    finance:0,//成本价
                    income:0,//售价
                    cost:0,//初始库存
                    reason: ''
                },
                ruleValidate: {                 
                    finance:[
                        
                        {type:'number',message:'只能输入数字'}
                    ],
                     income:[
                  
                        {type:'number',message:'只能输入数字'}
                    ],
                     cost:[
                      
                        {type:'number',message:'只能输入数字'}
                    ],
                    reason: [
                        { required: false, message: '请输入修改财务的理由', trigger: 'blur' },
                        { type: 'string', message: '描述不能少于20个字符', trigger: 'blur' }
                    ]
                }

            }
        },
          created(){           
            axios.get([g.http,'/finance/get'].join('')).then(
                                                    (res)=>{
                                                       this.formValidate=res.data.body;  
                                                       console.log(res) 
                                                        
                                                       

                        });
        },
        methods: {
            handleSubmit (name) {
                
                this.$refs[name].validate((valid) => {
                    if (valid) {
                                var data = {
                                            
                                            cost:this.formValidate.cost,
                                            income:this.formValidate.income,
                                            finance:this.formValidate.finance,
                                            reason:this.formValidate.reason,                                            
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
                                                        if(u.ajaxCallBack(res,'财务修改成功！',this.$Message))
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
