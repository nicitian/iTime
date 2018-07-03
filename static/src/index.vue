<style scoped>

    .layout-header-bar{
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .layout{
        border: 1px solid #ffffff;
        background: gray;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        height: 100%;
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
        width: 600px;
        margin: 0 auto;
        margin-right: 20px;
    }

    .m-layout-nav{        
        margin: 0px 5px;
        padding: 0px 0px;
        
    }

    .layout-footer-center{
        text-align: center;
    }
     .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;        
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
    .affix-menu-li li{
        width:80px;     
        padding-left:0px;
        padding-right:0px;  
    }

</style>
<template>
    <Row>
        <Col>
        <Layout class="layout" v-model="isMobile">
            <!-- <Header v-if="isMobile === true" :style="{width:'100%',padding:'0px 10px'}"> -->
              
            
            <!-- </Header> -->
            <Header v-if="isMobile === false" :style="[{position: 'fixed', width: '100%'}]" >
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
                        <MenuItem name="partner" @click.native="clickHeader('partner')">                          
                            <Icon type="ios-people"></Icon>
                            合作伙伴
                        </MenuItem>
                        <MenuItem name="login">
                            <Dropdown  placement="bottom-end">                            
                                <a href="javascript:void(0)" @clidck.native="handleInfo">
                                    {{name}}
                                    <Icon type="arrow-down-b"></Icon>
                                </a>
                                <DropdownMenu slot="list">
                                    <DropdownItem @click.native="handleUser()">个人信息</DropdownItem>                                    
                                    <DropdownItem @click.native="handleLogout()">注销</DropdownItem>                                   
                                </DropdownMenu>
                            </Dropdown>                                 
                        </MenuItem>
                  </div>
                </Menu>                                                   
            </Header>              
                <Layout v-if="headerActive === 'showuser'">
                    <user-info></user-info>
                </Layout>     

                <Layout v-if="headerActive === 'hoursestore'">                    
                    <Content :style="layoutContent" >                              
                        <Row :style="layoutContentRow">
                        
                        <!-- <Col span="16" offset="4">-->
                        <Col 
                        :xs="{span:24}"
                        :sm="{span:24}"
                        :md="{offset:4,span:16}"
                        :lg="{offset:4,span:16}"                        
                        >
                            <Layout >
                                <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" :style="{background: '#ffffff'}"  >
                                    <Menu :active-name="selected"  width="auto" :class="menuitemClasses" class="isMobile" >                    
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
                                    <div slot="trigger"></div>                                
                                </Sider>   
                                <Content>
                                    <add-goods @changeSider="clickSider" v-if="selected === 'add'" :userid="userid" :isMobile="isMobile"></add-goods>
                                    <overview @changeSider="clickSider" v-if="selected === 'overview'" :goodsPage="globalData.goodsPage" :pid="pid" :isMobile="isMobile"></overview>
                                </Content>
                            </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>  

                <Layout v-if="headerActive === 'oprations'">
                     <Content :style="layoutContent" >     
                        <Row :style="layoutContentRow">
                            <Col 
                            :xs="{span:24}"
                            :sm="{span:24}"
                            :md="{offset:4,span:16}"
                            :lg="{offset:4,span:16}">        
                                <Layout >
                                    <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                    <Sider  hide-trigger breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" :style="{background: '#ffffff'}"  >
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
                                        <add-goods @changeSider="clickOprationsSider" v-if="selectedOpraions === 'queryOprations'" :userid="userid" :isMobile="isMobile"></add-goods>
                                        <all-op @changeSider="clickOprationsSider" v-if="selectedOpraions === 'allOprations'" :Page="globalData.goodschangePage" :pid="pid" :isMobile="isMobile"></all-op>
                                    </Content>
                                </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>

                <Layout v-if="headerActive === 'finance'">
                     <Content :style="layoutContent" >     
                        <Row :style="layoutContentRow">
                            <Col
                            :xs="{span:24}"
                            :sm="{span:24}"
                            :md="{offset:4,span:16}"
                            :lg="{offset:4,span:16}">        
                                <Layout >
                                    <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                    <Sider  hide-trigger breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" :style="{background: '#ffffff'}"  >
                                        <!-- <Menu :active-name="selectedOpraions"  width="auto" :class="menuitemClasses"> -->
                                        <Menu :active-name="selectedOpraions"  width="auto">
                                            <MenuItem name="allFinance" @click.native="clickFinanceSider('allFinance')">
                                                <Icon type="android-menu"></Icon>
                                                <span>所有财务</span>
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
                                        <overview-finance @changeSider="clickFinanceSider" v-if="selectedFinance === 'overviewFinance'" :userid="userid" :isMobile="isMobile"></overview-finance>
                                        <query-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'queryFinance'" :page="globalData.queryFinancePage" :userid="userid" :isMobile="isMobile"></query-fi>
                                        <all-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'allFinance'" :Page="globalData.goodschangePage" :pid="pid" :isMobile="isMobile"></all-fi>
                                        <op-fi @changeSider="clickFinanceSider" v-if="selectedFinance === 'opFinance'" :Page="globalData.goodschangePage" :pid="pid" :isMobile="isMobile"></op-fi>
                                    </Content>
                                </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>

                <Layout v-if="headerActive === 'partner'">
                     <Content :style="layoutContent" >     
                        <Row :style="layoutContentRow">
                            <Col
                                :xs="{span:24}"
                                :sm="{span:24}"
                                :md="{offset:4,span:16}"
                                :lg="{offset:4,span:16}">           
                                <Layout >
                                    <!-- <Sider hide-trigger breakpoint="md" collapsible :collapsed-width="78"  v-model="isCollapsed"> -->
                                    <Sider  hide-trigger breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" :style="{background: '#ffffff'}"  >
                                        <Menu :active-name="selectedOpraions"  width="auto"  >
                                            <MenuItem name="allPartner" @click.native="clickPartnerSider('allPartner')">
                                                <Icon type="android-menu"></Icon>
                                                <span>所有伙伴</span>
                                            </MenuItem>     
                                            <MenuItem name="addPartner" @click.native="clickPartnerSider('addPartner')">
                                                <Icon type="android-add"></Icon>
                                                <span>添加伙伴</span>
                                            </MenuItem>                                                           
                                            <!-- <MenuItem name="edit" @click.native="clickSider('edit')">
                                                <Icon type="edit"></Icon>
                                                <span>编辑商品</span>ini
                                            </MenuItem> -->
                                        </Menu>                                            
                                    </Sider>   
                                    <Content>
                                        <!-- <overview-finance @changeSider="clickPartnerSider" v-if="selectedFinance === 'overviewFinance'" :userid="userid"></overview-finance>
                                        <query-fi @changeSider="clickPartnerSider" v-if="selectedFinance === 'queryFinance'" :page="globalData.queryFinancePage" :userid="userid"></query-fi>
                                        <all-fi @changeSider="clickPartnerSider" v-if="selectedFinance === 'allFinance'" :Page="globalData.goodschangePage" :pid="pid"></all-fi> -->
                                        <add-partner @changeSider="clickPartnerSider" v-if="selectedPartner === 'addPartner'" :Page="globalData.goodschangePage" :pid="pid" :isMobile="isMobile"></add-partner>
                                        <all-partner @changeSider="clickPartnerSider" v-if="selectedPartner === 'allPartner'" :Page="globalData.goodschangePage" :pid="pid" :isMobile="isMobile"></all-partner>
                                    </Content>
                                </Layout>
                            </Col>
                        </Row>
                    </Content>
                </Layout>
            
              
            <Footer v-if="isMobile === false" class="layout-footer-center">2018-2020 &copy; ITime</Footer>
           
            <Affix :offset-top="heightView-60" :offset-bottom="0" v-if="isMobile === true" :style="{width:'100%'}">
                    <Menu 
                    ref="sidemenu"
                    mode="horizontal" 
                    theme="dark" 
                    :active-name="headerActive" 
                    accordion
                    class="affix-menu-li">     
                      <!-- @on-select="onSelect"
                    @on-open-change="onOpenChange" -->
                        <Row type="flex" justify="space-between">   
                            <Col >                
                                <MenuItem name="oprations" @click.native="clickHeader('oprations')" >
                                    <Icon type="ios-navigate"></Icon>
                                    操作
                                </MenuItem>
                                <!-- <MenuItem name="hoursestore" @click.native="clickStoreHouse()">
                                    <Icon type="ios-keypad"></Icon>
                                    仓库
                                </MenuItem> -->
                            </Col>
                            <Col >
                                <Submenu name="hoursestore">
                                    <template slot="title">
                                        <Icon type="ios-keypad"></Icon>
                                        仓库
                                    </template>    
                                    <MenuGroup title="选项" style="width:120px" >                        
                                        <MenuItem name="overview" @click.native="clickStoreHourseSider('overview')">
                                            <Icon type="ios-list" ></Icon>
                                            <span>仓库概览</span>
                                        </MenuItem>
                                        <MenuItem name="add" @click.native="clickStoreHourseSider('add')">
                                            <Icon type="android-add"></Icon>
                                            <span>添加商品</span>
                                        </MenuItem>   
                                    </MenuGroup>                        
                                </Submenu>
                            </Col>
                            <Col >
                                <Submenu name="finance">
                                    <template slot="title">
                                        <Icon type="ios-bars"></Icon>
                                        财务
                                    </template>    
                                    <MenuGroup title="选项" style="width:120px" >   
                                        <MenuItem name="allFinance" @click.native="clickFinanceSider('allFinance')">
                                                        <Icon type="android-menu"></Icon>
                                                        <span>所有财务</span>
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
                                    </MenuGroup>                        
                                </Submenu>
                            </Col>
                            <Col >
                            <!-- <MenuItem name="finance" @click.native="clickHeader('finance')">
                                <Icon type="stats-bars"></Icon>
                                财务
                            </MenuItem> -->
                                <Submenu name="partner">
                                    <template slot="title">
                                        <Icon type="ios-people"></Icon>
                                        伙伴
                                    </template>    
                                    <MenuGroup title="选项" style="width:120px" >                        
                                        <MenuItem name="allPartner" @click.native="clickPartnerSider('allPartner')">
                                            <Icon type="android-menu"></Icon>
                                            <span>所有伙伴</span>
                                        </MenuItem>     
                                        <MenuItem name="addPartner" @click.native="clickPartnerSider('addPartner')">
                                            <Icon type="android-add"></Icon>
                                            <span>添加伙伴</span>
                                        </MenuItem>     
                                    </MenuGroup>                        
                                </Submenu>
                            </Col>                            
                            <!-- <MenuItem name="partner" @click.native="clickHeader('partner')">                          
                                <Icon type="ios-people"></Icon>
                                伙伴
                            </MenuItem>         
                                        -->
                        </Row>
                  </Menu>
                </Affix>                
            </Layout>
        </Col>        
    </Row>
    
</template>
<script>
    import axios from 'axios';
    import g from './libs/global.js';
    import addGoods from './index/storehouse/addGoods.vue';
    import overview from './index/storehouse/overview.vue';
    import allOp from './index/oprations/alloprations.vue';    
    import overviewFinance from './index/finance/overviewfinance.vue';
    import allFi from './index/finance/allfinance.vue';
    import opFi from './index/finance/opfinance.vue';
    import queryFi from './index/finance/queryfinance.vue';
    import addPartner from './index/partner/addpartner.vue';
    import allPartner from './index/partner/allpartner.vue';
    import userInfo from './index/user/edituser.vue';
    
    export default {
        components:{addGoods,overview,allOp,overviewFinance,allFi,opFi,queryFi,addPartner,allPartner,userInfo},
        mounted(){
            // let open_names = Cookies.getJSON('menu_opennames');
            // let active_name = Cookies.getJSON('active_name');
            // if(open_names || active_name){
            //     this.openNames = open_names || [];
            //     this.activeName = active_name || 0;
            //     this.$nextTick(()=>{
            //         this.$refs.side_menu.updateOpened();
            //         this.$refs.side_menu.updateActiveName()
            //     })
            // }
            this.$nextTick(()=>{
                    this.$refs.sidemenu.updateOpened();
                    this.$refs.sidemenu.updateActiveName()
                })
        },
        methods:{
            handleInfo(){
                ;
            },
            handleUser(){
                this.headerActive = "showuser"
            },
            handleLogout(){
                
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
                this.headerActive = 'finance';
                this.selectedFinance = name;
            }
            ,
            clickPartnerSider(name){
                this.headerActive = 'partner';
                this.selectedPartner = name;  
                console.log(this.$refs.sidemenu)                    
            },
            clickStoreHourseSider(name)
            {
                this.headerActive = 'hoursestore';
                this.selected = name;
                
                
            },
            clickStoreHouse(){
                
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
               isMobile:window.innerWidth >= 992 ? false :true,
                xs:768,
                sm:992,
                md:1200,
                isCollapsed:false,
                withView:window.innerWidth,
                heightView:window.innerHeight,
                name:"……",
                pid:1,
                logoUrl:'../static/images/logo1.png',
                selected:'overview',
                selectedOpraions:'allOprations',
                selectedFinance:'allFinance',
                selectedPartner:'allPartner',
                headerActive:'hoursestore',
                globalData:{
                    goodsPage:'1',
                    goodschangePage:'1',
                    queryFinancePage:'1',

                }                
            }
        },      
         computed: {  
            layoutContent:function(){
                let mdStyle = {margin: '88px 20px 0', minHeight: '500px'}
                let smStyle = {margin: '0px 0px 0px', minHeight: '80%'}
                // <Content :style="{margin: '88px 20px 0', minHeight: '500px'}" >                              
                //         <Row :style="{margin: '64px 0px 0px'}">
                return this.isMobile?smStyle:mdStyle;
            }   ,       
            layoutContentRow:function(){
                let mdStyle = {margin: '64px 0px 0px'}
                let smStyle = {margin: '0px 0px 0px'}
                return this.isMobile?smStyle:mdStyle;
            },
            menuitemClasses: function () {
                return [
                    'menu-item',
                    this.isCollapsed ? 'collapsed-menu' : ''
                ]
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
