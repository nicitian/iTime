<template>
    <Row :style="rowStyle">
        <!-- <Col span="12" offset="4"> -->
        <Col :xs="{offset:2,span:18}" :md="{offset:10,span:4}"> 
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                
                <Row>
                    <Col 
                        :xs="{span:18}"
                        :md="{span:12}">
                        <FormItem label="商品名字" prop="name">
                            <Input v-model="formValidate.name" placeholder="请输入商品名字"></Input>
                        </FormItem>
                    </Col>
                </Row>
                <FormItem label="进价" prop="costprice">
                    <!-- <Inputnumber v-model="formValidate.costprice" placeholder="请填入产品进价"></Input> -->
                    <Input-number  :min="0" v-model="formValidate.costprice" placeholder="请填入产品进价"></Input-number>
                </FormItem>
                <FormItem label="售价" prop="saleprice">
                    <!-- <Input v-model="formValidate.saleprice" placeholder="请填入产品售价"></Input> -->
                    <Input-number  type="number" :min="0" v-model="formValidate.saleprice" placeholder="请填入产品售价"></Input-number>
                </FormItem>
                <FormItem label="初始库存" prop="initotal">
                    <!-- <Input v-model="formValidate.initotal" placeholder="请填入初始库存"></Input> -->
                    <Input-number  :min="0" v-model="formValidate.initotal" placeholder="请填入初始库存"></Input-number>
                </FormItem>
                
                <FormItem label="描述" prop="desc">
                    <Input v-model="formValidate.desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入商品描述"></Input>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="handleSubmit('formValidate')">添加</Button>
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
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    export default {
        data () {
            return {
                rowHight:[window.innerHeight-60].join('px'),
               isMobile:window.innerWidth >= 992 ? false :true,               
                formValidate: {
                    name: '',
                    costprice:0,//成本价
                    saleprice:0,//售价
                    initotal:0,//初始库存
                    desc: ''
                },
                ruleValidate: {
                    name: [
                        { required: true, message: '名字不能为空', trigger: 'blur' }
                    ],
                    costprice:[
                        
                        {type:'number',message:'只能输入数字'}
                    ],
                     saleprice:[
                  
                        {type:'number',message:'只能输入数字'}
                    ],
                     initotal:[
                      
                        {type:'number',message:'只能输入数字'}
                    ],
                    desc: [
                        { required: false, message: '请输入关于商品的描述', trigger: 'blur' },
                        { type: 'string', min: 20, message: '描述不能少于20个字符', trigger: 'blur' }
                    ]
                }

            }
        },
        computed:{
           
            rowStyle(){
                return this.isMobile ? {
                    height:[this.rowHight,'px'].join(''), 
                    paddingTop:"100px"                   
                }:{}
            }
        },
        methods: {
            
            onOpenChange(name){
                //设置菜单展开子菜单的数组name
                Cookies.set('menu_opennames',name);
            },
            onSelect(name){        
                //设置菜单激活的name        
                Cookies.set('active_name',name);},
            handleSubmit (name) {
                
                this.$refs[name].validate((valid) => {
                    if (valid) {
                                var data = {
                                            name:this.formValidate.name,
                                            costprice:this.formValidate.costprice,
                                            saleprice:this.formValidate.saleprice,
                                            initotal:this.formValidate.initotal,
                                            desc:this.formValidate.desc,                                            
                                        };

                                data = qs.stringify(data);

                                axios.post(
                                            "/goods/create",
                                             data,
                                             {
                                                headers:{
                                                         'Content-Type':'application/x-www-form-urlencoded',                            
                                                         },
                                             }
                                        ).then(
                                                res =>{
                                                        if(u.ajaxCallBack(res,'商品添加成功！',this.$Message))
                                                            this.$emit('changeSider','overview');
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
