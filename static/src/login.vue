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
                            <Col :xs="{offset:2,span:20}" :md="{offset:10,span:4}">
                                <Row>
                                    <Col>
                                        <p align="center" class='login-alert'>
                                            欢迎登录
                                        </p>
                                    </Col>
                                </Row>
                                <Row>
                                    <Col >
                                        <Form ref="formInline" :model="formInline" :rules="ruleInline" >
                                            <FormItem prop="user">
                                                <Input type="text" v-model="formInline.user" placeholder="账户...">
                                                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                                                </Input>
                                            </FormItem>
                                            <FormItem prop="password">
                                                <Input type="password" v-model="formInline.password" placeholder="密码...">
                                                    <Icon type="ios-locked-outline" slot="prepend"></Icon>
                                                </Input>
                                            </FormItem>
                                            <FormItem>
                                                <layout>
                                                    <Row type='flex' justify='center'>
                                                        <Col >
                                                            <Button type="primary" @click="handleSubmit('formInline')">登录</Button>
                                                            <Button type="" @click="handleRegist()">注册</Button>
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
    import qs from 'qs';
    import addGoods from './index/storehouse/addGoods.vue';
    import overview from './index/storehouse/overview.vue';
    import allOp from './index/oprations/alloprations.vue';
    import g from './libs/global.js';
    import u from './libs/util.js';
    import overviewFinance from './index/finance/overviewfinance.vue';
    import allFi from './index/finance/allfinance.vue';
    import opFi from './index/finance/opfinance.vue';
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    export default {
        components:{addGoods,overview,allOp,overviewFinance,allFi,opFi},
        methods:{
            handleRegist(){
                window.location.href ='/login/toRegister_';
            },
            handleSubmit(name) {   
                let self = this.$Message                             
                console.log('call handlesumbmit!!!');
                this.$refs[name].validate((valid) => {
                    console.log(this.formInline);
                    if (valid) {
                                    console.log("合法！！");
                                    var data = {                                                        
                                                        account:this.formInline.user,                                            
                                                        password:this.formInline.password,
                                                                                            
                                                    };
                                    data = qs.stringify(data);
                                    axios.post(
                                                "/login/sumbit",
                                                data,
                                                {
                                                    headers:{
                                                            'Content-Type':'application/x-www-form-urlencoded',                            
                                                                },
                                                }
                                        ).then(
                                                res => {
                                                            console.log(res);
                                                            console.log(res.data.success)
                                                            if(res.data.success)
                                                            {
                                                               u.ajaxCallBack(res,res.data.info,self,true,res.data.toURL); 
                                                            }
                                                            else
                                                            {
                                                                u.ajaxCallBack(res,res.data.info,self);
                                                            }
                                                            // ajaxCallBack(res,'登录成功',self,true,'/login/index');
                                                            }
                                            );
                    } else {
                        this.$Message.error('Fail!');
                    }
                })
            },
            handleInfo(){
                console.log("handleInfo");
            },
            handleLogout(){
                console.log("单击 注销");
                axios.get('/login/logout').then(
                   () => {window.location.href = '/login/index'} 
                )
            },
            clickHeader(actName){
                this.headerActive = actName;
            },
            clickOprationsSider(name){
                this.selectedOpraions = name;
            },
            clickFinanceSider(name){
                this.selectedFinance = name;
            }
            ,
            clickStoreHouse(){
                console.log("trgger clickStoreHouse");
                this.headerActive = 'hoursestore'
                this.selected = 'overview';
            },
            clickSider(res,goodsPage=this.globalData.goodsPage){                
                this.selected = res;    
                this.globalData.goodsPage = goodsPage;         
            }
        },
        data () {
            return {
                logoUrl:'../static/images/logo1.png',
                formInline: {
                    user: '',
                    password: ''
                },
                ruleInline: {
                    user: [
                        { required: true, message: '请填入账户...', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请填入密码', trigger: 'blur' },
                        { type: 'string', min: 6, message: '密码至少需要6位', trigger: 'blur' }
                    ]
                }
            }
        },
        created(){
            // axios.get([g.http,"/login/getS?name=account"].join('')).then(res=>{
            //                                                                     console.log('account-get',res.data);
            //                                                                     this.name = res.data.name;
            //                                                                     this.pid = res.data.id;
            //                                                                 });
            
        }
    }
</script>
