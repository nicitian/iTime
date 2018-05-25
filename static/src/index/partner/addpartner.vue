<template>
    <Row>
        <Col span="12" offset="4">
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                <Row>
                    <Col span="8">
                        <FormItem label="合作伙伴" prop="name">
                            <Input v-model="formValidate.name" placeholder="合作伙伴的名字"></Input>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="4">
                        <FormItem label="合作关系" prop="relation">                    
                            <Select v-model="formValidate.relation" style="width:80px" >
                                <Option v-for="item in formValidate.typesList" :value="item.value" :key="item.value">{{item.value}}</Option>            
                            </Select>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="4">
                        <FormItem label="合作商品"  prop="goods">                        
                            <Select 
                                v-model="formValidate.goods"
                                multiple 
                                filterable
                                remote
                                :remote-method="goodsRemote"
                                :loading="formValidate.goodsLoadings"
                                placeholder="请输入商品名并选择"
                                style="width:220px">
                                <Option v-for="item in formValidate.goodsOpts" :value="item.id" :key="item.id">{{item.value}}</Option>            
                            </Select>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <FormItem label="负责人" prop="charge_person">
                            <Input v-model="formValidate.charge_person" placeholder="负责人名字"></Input>
                        </FormItem>
                    </Col>
                </Row>
                
                <Row>
                    <Col span="8">
                        <FormItem label="手机号码" prop="phone_number">
                            <Input v-model="formValidate.phone_number" placeholder="合作伙伴联系方式"></Input>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="24">
                        <FormItem label="地址" prop="address">
                            <Input v-model="formValidate.address" placeholder="合作伙伴地址"></Input>
                        </FormItem>
                    </Col>
                </Row>                            
                <FormItem label="备注" prop="remark">
                    <Input v-model="formValidate.remark" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入备注信息"></Input>
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
    import g from '../../libs/global.js';
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    export default {
        data () {
            return {
                formValidate: {
                    goodsLoadings:false,    
                    goodsOpts:[],                                
                    typesList:[
                        {
                            value:'供应商',
                            lable:'供应商'                          
                        },
                        {
                            value:'采购商',
                            lable:'采购商'
                        },
                        {
                            value:'其他',
                            lable:'其他'
                        }
                    ],
                    goods_types:[
                        {
                            value:'可乐',
                            lable:'可乐'                          
                        },
                        {
                            value:'雪碧',
                            lable:'雪碧'
                        },
                        {
                            value:'芬达',
                            lable:'芬达'
                        }
                    ],
                    name: '',
                    phone_number:'',
                    charge_person:'',
                    weixin:'',
                    address:'',//售价
                    supplier:'',
                    purchaser:'',
                    relation:'',
                    goods:[],                        
                    remark: ''
                },
                ruleValidate: {
                    name: [
                        { required: true, message: '名字不能为空', trigger: 'blur' },
                        {max:50}                                            
                    ],
                    phone_number: [
                        { message: '请输入电话号码', trigger: 'blur' },
                        {max:30}
                    ],
                    charge_person: [
                        { message: '请输入负责人', trigger: 'blur' },
                        {max:50}
                    ],
                    weixin: [
                        { message: '请输入微信', trigger: 'blur' },
                        {max:50}
                    ],
                    address: [
                        {  message: '请输入合作关系', trigger: 'blur' }
                        ,{max:100}
                    ],                   
                    relation: [
                        {type:'string',required:true,message:'操作类型为必填项'}
                    ],
                   
                    remark: [
                        { message: '请输入关于商品的描述', trigger: 'blur' },
                        { type: 'string', message: '描述不能少于20个字符', trigger: 'blur' }
                    ]
                }

            }
        },
        methods: {
            goodsRemote(query){
                 if (query != '') {
                    this.formValidate.goodsLoadings = true;
                    setTimeout(() => {
                        
                        axios.get([g.http,'/goods/query',"?name=",query].join('')).then(
                                                    (res)=>{
                                                        console.log(res);
                                                        this.formValidate.goodsLoadings = false;
                                                       this.formValidate.goodsOpts = res.data;
                        });
                    }, 200);
                } else {
                    this.formValidate.goodsOpts = [];
                }
            },
            handleSubmit (name) {
                
                this.$refs[name].validate((valid) => {
                    if (valid) {
                                var data = {
                                            name:this.formValidate.name,
                                            address:this.formValidate.address,
                                            relation:this.formValidate.relation,
                                            goods:this.formValidate.goods.join(','),
                                            charge_person:this.formValidate.charge_person,    
                                            remark:this.formValidate.remark,
                                            phone_number:this.formValidate.phone_number                                        
                                        };

                                data = qs.stringify(data);

                                axios.post(
                                            "/partner/create",
                                             data,
                                             {
                                                headers:{
                                                         'Content-Type':'application/x-www-form-urlencoded',                            
                                                         },
                                             }
                                        ).then(
                                                res =>{
                                                        if(u.ajaxCallBack(res,'合作伙伴添加成功！',this.$Message))
                                                            this.$emit('changeSider','allPartner');
                                                }
                                            );
                        
                    } else {
                        this.$Message.error('填写有误!');
                    }
                })
            },
            handleReset (name) {
                this.$refs[name].resetFields();
                this.formValidate.goods = [];
            }
        }
    }
</script>
