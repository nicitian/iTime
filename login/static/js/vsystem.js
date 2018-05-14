temp=''
Vue.component('new-body', {
    props:['q'],
 	template: '<tr>\n' +
    '                                            <th socpe="row">{{ q.id }}</th>\n' +
    '                                            <td>{{ q.name }}</td>\n' +
    '                                            <td>{{ q.type }}</td>\n' +
    '                                            <td>{{ q.content }}</td>\n' +
    '                                            <td class="text-center" >\n' +
    '                                                <a href="../questions/show/edit?q_id={{ q.id }}"> 编辑</a>|\n' +
    '                                                <a>删除</a>\n' +
    '                                            </td>\n' +
    '                                        </tr>'
})

Vue.component('new',{
    template:'<p>new p-tag!</p>'
})
Vue.component('todo-item', {
	props:['todo'],
 	template: '<li>{{todo.text}}</li>'
})
var app = new Vue({
          el:"#app",
          data:{
            msg:'abc',
            todos:[
            {id:0,text:'蔬菜'},
            {id:1,text:'水果'},
            {id:2,text:'肉类'}]
          },
          computed:{
          	rMsg:function(){
          		return this.msg.split('').reverse().join('')
          	}
          }
        })
var vform = new Vue({
    el:"#vform",
    data:{
        account:"1",
        password:"2",
    }
})
var Qajax = axios.create({
    baseURL:"http://localhost:8000/questions/"
})
var vtbody = new Vue({
                        el:"#vuetbody",
                        data:{
                               questions:[]
                              },
                        mounted:function (){
                            console.log("mounted!!!")
                            Qajax.interceptors.response.use(function (res) {
                                                 console.log("instance use",res.data)
                                                 vtbody.questions = res.data
                                                })
                                Qajax.get('get')
                        }
})

//vtbody.questions  = [{name:1,type:1,id:1,content:1}]


