<template>
                     
        <Row :style="divHeight">
                    <Col                         
                        :sm="{span:24}"                        
                        :md="{span:8,offset:8}">

                        <Card :style="divHeight">
                            <p  slot="title" align="center" class='login-alert'>
                                    个人信息
                            </p>         
                            <Form ref="formInline" :model="formInline"  :rules="ruleInline" :label-width="80"  method="post">                                                
                                <FormItem prop="user" label="用户名">
                                    <Input readonly type="text" v-model="formInline.user" placeholder="用户名、账户"></Input>
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
                                        
                                            <Row type='flex' justify='center'>
                                                <Col span="24">
                                                    <Button type="primary" @click="handleSubmit('formInline')">修改</Button>
                                                    <Button type="" @click="handleBack()">重置</Button>
                                                </Col>
                                            </Row>
                                        
                                </FormItem>  
                            </Form>
                        </Card>   
                    </Col>
                </Row>
                      
                                        
</template>
<script>
import axios from 'axios';
import g from '../../libs/global.js';
import qs from 'qs';
import u from '../../libs/util.js';  
axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
export default {
    props:['isMobile'],
    data(){
        
        return {
                logoUrl:'../static/images/logo1.png',
                formInline: {
                    user: '',   
                    isMobile:window.innerWidth >= 992 ? false :true,               
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
                    phoneNumber:[
                        {type:'string',max:50}
                    ],
                    qqNumber:[
                        {type:'string',max:50}
                    ],
                    weixinNumber:[
                        {type:'string',max:50}
                    ],                    
                    mail:[
                        { required: true, message: '邮箱不能为空 ', trigger: 'blur' },
                        { type: 'email', message: '邮箱格式不正确', trigger: 'blur' }
                    ]
                }
            }
    },
    created(){
        axios.get([g.http,'/login/getUser'].join('')).then(
                                                    (res)=>{
                                                        console.log(res.data);
                                                       this.formInline = res.data;
                        });
    },
    computed:{
         heightView(){
                let height = window.innerHeight - 60;
                return this.isMobile? height:600;
            },
        contentHight(){
                let sm = {}
                let md ={margin: '88px 20px 0', minHeight: '800px'}
                return this.isMobile? sm : md;
            },
            divHeight(){
                let height = window.innerHeight;
                height = height - 60;
                
                console.log("log:"+height);
                return {
                    height:this.isMobile?height+'px':'600px' ,
                    width:'100%'
                }
            }
    },
    methods:{
        handleBack()
        {
            axios.get([g.http,'/login/getUser'].join('')).then(
                                                    (res)=>{
                                                        console.log(res.data);
                                                       this.formInline = res.data;
                        });
        },
         handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        let self =  this.$Message
                        var data = {
                                                                
                                        phoneNumber:this.formInline.phoneNumber,
                                        weixinNumber:this.formInline.weixinNumber,
                                        qqNumber:this.formInline.qqNumber,
                                        mail:this.formInline.mail
                            }
                        data = qs.stringify(data)
                        axios.post(
                                    [g.http,"/login/updateUser"].join(''),
                                    data,
                                    {
                                    headers:{'Content-Type':'application/x-www-form-urlencoded'},
                                    }
                                ).then(
                                        res =>{
                                                u.ajaxCallBack(res,'修改成功！',self,false);
                                                axios.get([g.http,'/login/getUser'].join('')).then(
                                                            (res)=>{
                                                                console.log(res.data);
                                                            this.formInline = res.data;
                                                            });                                        
                                        }
                                    );
                    } else {
                        this.$Message.error('填写有误!');
                    }
                })

                
            },
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
