<template>
    <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="80" action="Regist" method="post">
        <h1><Alert show-icon style="text-align:center">欢迎注册！！！</Alert></h1>
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
            <Button type="primary" @click="handleSubmit(formInline)">提交</Button>
        </FormItem>  
    </Form>
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
            handleSubmit(name) {
                // var params = new URLSearchParams()
                // params.append('account',name.user)
                // params.append('password',name.password)

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
                        ).then(res =>u(res,'注册成功！',this.$Message,back=true,'/login/index'));
            },
            handleRegist(name){
                console.log("press 注册")
            }
        }
    }
</script>
<style>
</style>
