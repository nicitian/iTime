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
</style>
<template>
    <div class="layout">
        <Layout>
            <Header :style="{position: 'fixed', width: '100%'}" >
                <Menu mode="horizontal" theme="dark" :active-name="headerActive">
                  <img  class="layout-logo"  :src="logoUrl" alt="logo" />
                  <div class="layout-nav">
                       <MenuItem name="oprations" @click.native="clickHeader('oprations')">
                            <Icon type="ios-navigate"></Icon>
                            最近操作
                        </MenuItem>
                        <MenuItem name="hoursestore" @click.native="clickStoreHouse()">
                            <Icon type="ios-keypad"></Icon>
                            仓库
                        </MenuItem>
                        <MenuItem name="finance" @click.native="clickHeader('finance')">
                            <Icon type="stats-bars"></Icon>
                            财务
                        </MenuItem>
                        <!-- <MenuItem name="person" @click.native="clickHeader('person')">                          
                            <Icon type="ios-people"></Icon>
                            人员
                        </MenuItem> -->
                        <MenuItem name="login">
                            <Dropdown  placement="bottom-end">                            
                                <a href="javascript:void(0)" @clidck.native="handleInfo">
                                    {{name}}
                                    <Icon type="arrow-down-b"></Icon>
                                </a>
                                <DropdownMenu slot="list">
                                    <!-- <DropdownItem @click.native="handleInfo()">个人信息</DropdownItem>                                     -->
                                    <DropdownItem @click.native="handleLogout()">注销</DropdownItem>                                   
                                </DropdownMenu>
                            </Dropdown>
                                 
                        </MenuItem>
                  </div>
                </Menu>                                                   
            </Header>               
                <Layout v-if="headerActive === 'hoursestore'">                    
                    <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}" >     
                        <Row :style="{margin: '64px 0px 0px'}">
                        <Col span="16" offset="4">        
                            <Layout >
                                <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                <Sider hide-trigger breakpoint="md" :style="{background: '#fff'}"  >
                                    <Menu :active-name="selected"  width="auto" >                    
                                        <MenuItem name="overview" @click.native="clickSider('overview')">
                                            <Icon type="ios-list"></Icon>
                                            <span>仓库概览</span>
                                        </MenuItem>
                                        <MenuItem name="add" @click.native="clickSider('add')">
                                            <Icon type="android-add"></Icon>
                                            <span>添加商品</span>
                                        </MenuItem>
                                        <!-- <MenuItem name="edit" @click.native="clickSider('edit')">
                                            <Icon type="edit"></Icon>
                                            <span>编辑商品</span>
                                        </MenuItem> -->
                                    </Menu>                                            
                                </Sider>   
                                <Content>
                                    <add-goods @changeSider="clickSider" v-if="selected === 'add'" :userid="userid"></add-goods>
                                    <overview @changeSider="clickSider" v-if="selected === 'overview'" :goodsPage="globalData.goodsPage" :pid="pid"></overview>
                                </Content>
                            </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>  

                <Layout v-if="headerActive === 'oprations'">
                     <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}" >     
                        <Row :style="{margin: '64px 0px 0px'}">
                            <Col span="18" offset="3">        
                                <Layout >
                                    <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                    <Sider hide-trigger breakpoint="md" :style="{background: '#fff'}"  >
                                        <Menu :active-name="selectedOpraions"  width="auto" >                    
                                            <MenuItem name="allOprations" @click.native="clickOprationsSider('allOprations')">
                                                <Icon type="android-menu"></Icon>
                                                <span>所有操作</span>
                                            </MenuItem>
                                            <!-- <MenuItem name="queryOprations" @click.native="clickOprationsSider('queryOprations')">
                                                <Icon type="android-search"></Icon>
                                                <span>操作查询</span>
                                            </MenuItem> -->
                                            <!-- <MenuItem name="edit" @click.native="clickSider('edit')">
                                                <Icon type="edit"></Icon>
                                                <span>编辑商品</span>
                                            </MenuItem> -->
                                        </Menu>                                            
                                    </Sider>   
                                    <Content>
                                        <add-goods @changeSider="clickOprationsSider" v-if="selectedOpraions === 'queryOprations'" :userid="userid"></add-goods>
                                        <all-op @changeSider="clickOprationsSider" v-if="selectedOpraions === 'allOprations'" :Page="globalData.goodschangePage" :pid="pid"></all-op>
                                    </Content>
                                </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>

                <Layout v-if="headerActive === 'finance'">
                     <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}" >     
                        <Row :style="{margin: '64px 0px 0px'}">
                            <Col span="18" offset="3">        
                                <Layout >
                                    <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                    <Sider hide-trigger breakpoint="md" :style="{background: '#fff'}"  >
                                        <Menu :active-name="selectedOpraions"  width="auto" >
                                            <MenuItem name="allFinance" @click.native="clickFinanceSider('allFinance')">
                                                <Icon type="android-menu"></Icon>
                                                <span>所有财务记录</span>
                                            </MenuItem>     
                                            <MenuItem name="overviewFinance" @click.native="clickFinanceSider('overviewFinance')">
                                                <Icon type="android-open"></Icon>
                                                <span>财务总览</span>
                                            </MenuItem>               
                                            <MenuItem name="opFinance" @click.native="clickFinanceSider('opFinance')">
                                                <Icon type="edit"></Icon>
                                                <span>财务操作</span>
                                            </MenuItem>
                                            <MenuItem name="queryFinance" @click.native="clickFinanceSider('queryFinance')">
                                                <Icon type="android-search"></Icon>
                                                <span>财务查询</span>
                                            </MenuItem>
                                            <!-- <MenuItem name="edit" @click.native="clickSider('edit')">
                                                <Icon type="edit"></Icon>
                                                <span>编辑商品</span>ini
                                            </MenuItem> -->
                                        </Menu>                                            
                                    </Sider>   
                                    <Content>
                                        <overview-finance @changeSider="clickFinanceSider" v-if="selectedFinance === 'overviewFinance'" :userid="userid"></overview-finance>
                                        <query-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'queryFinance'" :page="globalData.queryFinancePage" :userid="userid"></query-fi>
                                        <all-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'allFinance'" :Page="globalData.goodschangePage" :pid="pid"></all-fi>
                                        <op-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'opFinance'" :Page="globalData.goodschangePage" :pid="pid"></op-fi>
                                    </Content>
                                </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>

            </Layout>
            <Footer class="layout-footer-center">2018-2020 &copy; ITime</Footer>

    </div>
</template>
<script>
    import axios from 'axios';
    import addGoods from './index/storehouse/addGoods.vue';
    import overview from './index/storehouse/overview.vue';
    import allOp from './index/oprations/alloprations.vue';
    import g from './libs/global.js';
    import overviewFinance from './index/finance/overviewfinance.vue';
    import allFi from './index/finance/allfinance.vue';
    import opFi from './index/finance/opfinance.vue';
    import queryFi from './index/finance/queryfinance.vue';
    export default {
        components:{addGoods,overview,allOp,overviewFinance,allFi,opFi,queryFi},
        methods:{
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
        data(){
            return {
                name:"……",
                pid:1,
                logoUrl:'../static/images/logo1.png',
                selected:'overview',
                selectedOpraions:'allOprations',
                selectedFinance:'allFinance',
                headerActive:'hoursestore',
                globalData:{
                    goodsPage:'1',
                    goodschangePage:'1',
                    queryFinancePage:'1',

                }
                
            }
        },
        created(){
            axios.get([g.http,"/login/getS?name=account"].join('')).then(res=>{
                                                                                console.log('account-get',res.data);
                                                                                this.name = res.data.name;
                                                                                this.pid = res.data.id;
                                                                            });
            
        }
    }
</script>
