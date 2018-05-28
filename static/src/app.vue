<style scoped>
    .layout{
        border: 1px solid #ffffff;
        /* background: #ffffff; */
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        height: 100%;
    }
    .layout-logo{
        width: 100px;
        height: 40px;
        background: #fdfdfd;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 6px;
        bottom: 6px;
        left: 20px;
    }
    .layout-nav{
        width: 420px;
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
            <Header :style="{position: 'fixed', width: '100%'}">
                <Menu mode="horizontal" theme="dark" active-name="1">
                  <img class="layout-logo" src="..static/dist/logo.png" alt="logo">
                </Menu>
            </Header>
            <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}">
                <Row type="flex" justify="center" align="middle" class="code-row-bg" style="height: 100%">
                    <Col span="4">
                        <template style="height: 80px">                            
                            <regist></regist>
                        </template>
                    </Col>
                </Row>
                
            </Content>
            <Footer class="layout-footer-center">2018-2020 &copy; ITime</Footer>
        </Layout>
    </div>
</template>
<script>
    import regist from './regist.vue'

    export default {
        components:{regist}
    }
</script>
