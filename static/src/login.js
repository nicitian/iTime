import Vue from 'vue';
import iView from 'iview';
import VueRouter from 'vue-router';
import Routers from './router';
import Util from './libs/util';
import login from './login.vue';
import 'iview/dist/styles/iview.css';


Vue.use(iView);
new Vue({
    el: '#app',
    render: h => h(login),
    
  
});
