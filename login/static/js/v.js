Vue.component('newTbody', {
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
        account:"",
        password:"",
    }
})

var vtbody = new Vue({
    el:"#vtbody",
    data:{
        questions:[
            {id:1,name:"aaa",type:"1111",content:"!!!!"},
            {id:2,name:"bbbb",type:"222",content:"@@@@"},
            ]
    }
})
