<template>
        
           
        
        <Row type="flex" justify="center">
            <Col span="24">
                <Row>
                    <Col span="24">
                        <Menu mode="horizontal" theme="dark" :style="{width:100+'%'}" >
                            <img  class="layout-logo"  :src="logoUrl" alt="logo" />
                        </Menu>
                    </Col>
                </Row>
                <Row>
                    <Col                         
                        :sm="{span:24}"                        
                        :md="{span:8,offset:8}">
                        <Card  >   
                            <p  slot="title" align="center" class='login-alert'>
                                    请填写注册信息
                            </p>                     
                            <Form ref="formInline" :model="formInline" :rules="ruleInline" :label-width="80" action="Regist" method="post">   
                                    <Row type="flex" justify="center">   
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}">                                            
                                        <FormItem prop="user" label="用户名">
                                            <Input type="text" v-model="formInline.user" placeholder="用户名、账户"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center">   
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}"> 
                                        <FormItem prop="password" label="密码">
                                            <Input type="password" v-model="formInline.password" placeholder="密码"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center"> 
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}">
                                        <FormItem prop="mail" label="e-mail">
                                            <Input type="mail" v-model="formInline.mail" placeholder="电子邮箱"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center"> 
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}">
                                        <FormItem prop="phoneNumber" label="手机号码">
                                            <Input type="phoneNumber" v-model="formInline.phoneNumber" placeholder="手机号码"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center"> 
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}">
                                        <FormItem prop="weixinNumber" label="微信号">
                                            <Input type="weixinNumber" v-model="formInline.weixinNumber" placeholder="微信号"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center"> 
                                    <Col
                                        :sm="{span:22}"
                                        :md="{span:12}">
                                        <FormItem prop="qqNumber" label="QQ">
                                            <Input type="qqNumber" v-model="formInline.qqNumber" placeholder="QQ号"></Input>
                                        </FormItem>
                                    </Col>
                                </Row>
                                <Row type="flex" justify="center"> 
                                    <Col
                                        :sm="{span:24}"
                                        :md="{span:24}">
                                        <FormItem>
                                            <!-- <Button type="primary" @click="handleSubmit(formInline)">提交</Button> -->
                                                
                                                    <Row type='flex' justify='center'>
                                                        <Col >
                                                            <Button type="primary" @click="handleSubmit('formInline')">提交</Button>
                                                            <Button type="" @click="handleBack()">返回</Button>
                                                        </Col>
                                                    </Row>
                                                
                                        </FormItem>  
                                    </Col>                        
                                </Row>
                            </Form>                       
                        </Card>   
                    </Col>
                </Row>
            </Col>
        </Row>                  
    
</template>



<script>
   import axios from 'axios';
   import u from './libs/util.js';
   import qs from 'qs';
   import g from './libs/global.js';
           
   axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    export default {
        data () {
            return {
                isMobile:window.innerWidth >= 992 ? false :true,
                logoUrl:'../static/images/logo1.png',
                formInline: {
                    user: '',
                    password: '',
                    phoneNumber:'',
                    mail:'',
                    weixinNumber:'',
                    qqNumber:'',

                },
                ruleInline: {
                    user: [
                        { required: true, message: '请输入用户名...', trigger: 'blur' },
                        {type:'string',min:1,message:"输入有误！",trigger:'blur'}
                    ],
                    password: [
                        { required: true, message: '请输入密码...', trigger: 'blur' },
                        { type: 'string', min: 6, message: '请输入至少6个字符！！', trigger: 'blur' }
                    ],
                    mail:[
                        { required: true, message: '邮箱不能为空 ', trigger: 'blur' },
                        { type: 'email', message: '邮箱格式不正确', trigger: 'blur' }
                    ]
                }
            }
        },
        computed:{
            contentHight(){
                let sm = {}
                let md ={margin: '88px 20px 0', minHeight: '800px'}
                return this.isMobile? sm : md;
            },
            divHeight(){
                let height = window.innerHeight
                return {
                    height:height+'px'
                }
            }
        },
        methods: {
            handleBack(){
                window.location.href ='/login';
            },
            handleSubmit(name) {        
                 this.$refs[name].validate((valid) => {
                    if (valid) {
                        let self =  this.$Message
                        var data = {
                                        account:this.formInline.user,
                                        password:this.formInline.password,
                                        phoneNumber:this.formInline.phoneNumber,
                                        weixinNumber:this.formInline.weixinNumber,
                                        qqNumber:this.formInline.qqNumber,
                                        mail:this.formInline.mail
                            }
                            data = qs.stringify(data)
                            axios.post(
                                        [g.http,"/login/Regist_"].join(''),
                                        data,
                                        {
                                        headers:{'Content-Type':'application/x-www-form-urlencoded'},
                                        }
                                    ).then(res =>u.ajaxCallBack(res,'注册成功！',self,true,'/login/index'));
                    } else {
                        this.$Message.error('填写有误!');
                    }
                })      
               
            },
            handleRegist(name){
                console.log("press 注册")
            }
        }
    }
</script>
<style scoped>
    .layout{
        border: 1px solid #ffffff;
        background: #ffffff;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-logo{
        width: 100px;
        height: 50px;
        background: #ffffff;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 6px;
        bottom: 6px;
        left: 20px;
    }
    .layout-nav{
        width: 520px;
        margin: 0 auto;
        margin-right: 20px;
    }
    .layout-footer-center{
        text-align: center;
    }
    .login-alert{
        font-family: "PingFang SC";
        font-size: 1em;
        color:#2d8cf0;        
    }
</style>