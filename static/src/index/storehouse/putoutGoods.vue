<template>
    <div>
        <br>
        <br>
        <Row class="fixedinfo">
            <Col span="5" offse="1" order="1">商品名字: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.name}}</Col>
        </Row>
        <br>        
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">进价: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.costprice}}</Col>
        </Row>
        <br>
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">售价: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.saleprice}}</Col>
        </Row>                
        <br>
        <Row class="fixedinfo">
            <Col span='5' offse="1" order="1">库存: </Col>
            <Col span="16" offset="2" order="2">{{rowdata.initotal}}</Col>
        </Row>        
        <br>
        <Row type="flex" align="middle" class="fixedinfo">
            <Col span='5' offse="1" order="1" class="success">出库数量:</Col>
            <Col span="6" offset="2" order="2">
                <InputNumber :min='0' :max="rowdata.initotal" v-model="count" autofocus @on-change="input"></InputNumber >
            </Col>
            <Col order="3">
                <p> （输入应小于库存）</p>
            </Col>
        </Row> 
        
        
    </div>
</template>
<script>
    export default {
        props:['rowdata','color'],
        data(){
            return {
                count:0,
            }
        },       
        methods:{
                input(num){
                              this.$emit('input',num);
                        }
        }
       
    }
</script>
<style scoped>
.fixedinfo div:first-of-type{
    text-align: right;
    font-weight: bold;
}
.fixedinfo div{
    font-size-adjust: inherit;    
}
.success{
    color:#19be6b;
}
</style>
