<template>
    <div class="layout">
        <Layout>
            <Header :style="{position: 'fixed', width: '100%'}" >
                <Menu mode="horizontal" theme="dark" :active-name="headerActive">
                  <img  class="layout-logo"  :src="logoUrl" alt="logo" />
                  
                </Menu>                                                   
            </Header>               
            <Layout>
                <Content :style="{margin: '88px 20px 0', minHeight: '800px'}" >   
                    <Layout>
                        <Row type="flex" align="middle" :style="{minHeight:'700px'}">
                            <Col span='4' offset='10'> 
                                <Row>
                                    <Col>
                                        <p align="center" class='login-alert'>
                                            请填写注册信息！
                                        </p>
                                    </Col>
                                </Row>
                                <Row :style="{height:'20px'}">
                                </Row>                               
                                <Row>
                                    <Col >
                                            <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="80" action="Regist" method="post">                                                
                                                <FormItem prop="user" label="用户名">
                                                    <Input type="text" v-model="formInline.user" placeholder="用户名、账户"></Input>
                                                </FormItem>
                                                <FormItem prop="password" label="密码">
                                                    <Input type="password" v-model="formInline.password" placeholder="密码"></Input>
                                                </FormItem>
                                                <FormItem prop="mail" label="e-mail">
                                                    <Input type="mail" v-model="formInline.mail" placeholder="电子邮箱"></Input>
                                                </FormItem>
                                                <FormItem prop="phoneNumber" label="手机号码">
                                                    <Input type="phoneNumber" v-model="formInline.phoneNumber" placeholder="手机号码"></Input>
                                                </FormItem>
                                                <FormItem prop="weixinNumber" label="微信号">
                                                    <Input type="weixinNumber" v-model="formInline.weixinNumber" placeholder="微信号"></Input>
                                                </FormItem>
                                                <FormItem prop="qqNumber" label="QQ">
                                                    <Input type="qqNumber" v-model="formInline.qqNumber" placeholder="QQ号"></Input>
                                                </FormItem>
                                                <FormItem>
                                                    <!-- <Button type="primary" @click="handleSubmit(formInline)">提交</Button> -->
                                                        <layout>
                                                            <Row type='flex' justify='center'>
                                                                <Col >
                                                                    <Button type="primary" @click="handleSubmit(formInline)">提交</Button>
                                                                    <Button type="" @click="handleBack()">返回</Button>
                                                                </Col>
                                                            </Row>
                                                        </Layout>
                                                </FormItem>  
                                            </Form>
                                    </Col>
                                </Row>
                        </Col>
                        </Row>
                    </Layout>  
                </Content>
            </Layout>
        </Layout>
        <Footer class="layout-footer-center">2018-2020 &copy; ITime</Footer>

    </div>
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
        methods: {
            handleBack(){
                window.location.href ='/login';
            },
            handleSubmit(name) {
                // var params = new URLSearchParams()
                // params.append('account',name.user)
                // params.append('password',name.password)
                let self =  this.$Message
               var data = {
                            account:name.user,
                            password:name.password,
                            phoneNumber:name.phoneNumber,
                            weixinNumber:name.weixinNumber,
                            qqNumber:name.qqNumber,
                            mail:name.mail
                }
                data = qs.stringify(data)
                axios.post(
                            [g.http,"/login/Regist_"].join(''),
                             data,
                             {
                              headers:{'Content-Type':'application/x-www-form-urlencoded'},
                             }
                        ).then(res =>u.ajaxCallBack(res,'注册成功！',self,true,'/login/index'));
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
        font-size: 2em;
        color:#2d8cf0;        
    }
</style>