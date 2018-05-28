from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from questions.models import Questions
import functools
import json
import  json
# Create your views here.
from .models import Account

def getUser(request):
    user = request.session.get('user',False)
    user = user if user else Account.objects.get(id=1)
    res = {
            'user':user.account,
            'phoneNumber':user.phoneNumber if user.phoneNumber else '',
            'weixinNumber':user.weixinNumber if user.weixinNumber else '',
            'qqNumber':user.qqNumber if user.qqNumber else '',
            'mail':user.mail if user.mail else ''
    }
    return HttpResponse(json.dumps(res), content_type="application/json")

def updateUser(request):
    user = request.session.get('user', False)
    user = user if user else Account.objects.get(id=1)
    def update(obj):
        print("obj[1]=",obj[1])
        if obj[1] != False:
            setattr(user,obj[0],obj[1])


    data = {
        'phoneNumber':request.POST.get('phoneNumber',False),
        'qqNumber':request.POST.get('qqNumber',False),
        'weixinNumber':request.POST.get('weixinNumber',False),
        'mail':request.POST.get('mail',False),
    }

    list(map(update,data.items()))
    print(data)
    user.save()
    res = {'success':True}
    request.session['user'] = user
    return HttpResponse(json.dumps(res), content_type="application/json")


def dec_login(func):
    def wrapper(request,*args,**kw):
        if request.session.get("",False):
            pass
        return func(request,*args,**kw)
    return wrapper

def showLoginPage(request):
    return render(request,'login/login_.html',{'ok':False})

def submit(request):
    print("----------------",request.POST)
    account = request.POST['account']
    password = request.POST['password']
    print(account,password)
    q = Account.objects.filter(account=account,password=password).first()
    if q:
        request.session['login'] = True
        request.session['user'] = q
        res = {'success':True,'info':'登录成功',"toURL":"/login/index"}
        return HttpResponse(json.dumps(res), content_type="application/json")
    else:
        res = {'success':False,'err':'账号或密码输入有误！！！','info':'账号或密码输入有误!!'}
        return HttpResponse(json.dumps(res), content_type="application/json")

def questionmanager(request):
    Qs = Questions.objects.all()
    print(Qs)
    if request.session.get('login',False):
        return render(request,'QuestionManager.html',{'user':request.session['user'],'pageContent':"查看内容",'questions':Qs})
    else:
        return render(request,'login/login_.html',{'err':True})

def newQuestion(request):
    pageContent = "名字重复，请重新创建！" if request.GET.get('err','false')=='True' else "创建内容"
    if request.session.get('login',False):
        return render(request,'NewQuestion.html',{'user':request.session['user'],'pageContent':pageContent})
    else:
        return render(request,'login/login_.html',{'err':True})

def index(request):
    # print(request.session.get('login',False))
    # print(request.session.get('user',False))
    if request.session.get('login',False):
        return render(request,'index_.html',{'user':request.session['user']})
    else:
        return render(request,'login/login_.html',{'err':True,'info':"请先登录！！！"})

def index_(request):
    return HttpResponseRedirect('login/index')

def logout(request):
    del request.session['login']
    del request.session['user']
    return HttpResponseRedirect('/login/index')

def showRegisterPage(request):
    return render(request,'register_.html',{'repeatd':False})
def showRegisterPage_(request):
    return render(request,'register_.html',{'repeatd':False})

def isRegisted(request):
    account = request.GET.get('account')
    q = Account.objects.filter(account=account)
    res = True if q is None else False
    print("ok")
    return HttpResponse(json.dumps({'yes':False}), content_type="application/json")

def Regist(request):
    print("---------------",request.POST)
    account = request.POST.get('account')
    password = request.POST.get('password')
    mail = request.POST.get('mail')
    qq = request.POST.get('qqNumber', '')
    weixin = request.POST.get('weixinNumber', '')
    mobile = request.POST.get('phone_number', '')
    q = Account.objects.filter(account=account)
    if q :
        return render(request,'register.html',{'repeatd':True})
    else:

        newAccount=Account(account=account,password=password,mail=mail,qqNumber=qq,weixinNumber=weixin,phoneNumber=mobile)
        newAccount.save()
        return  render(request,'login/login_.html',{'ok':True})

def RegistApi(request):
    print("---------------",request.POST)
    account = request.POST.get('account')
    password = request.POST.get('password')
    mail = request.POST.get('mail')
    qq = request.POST.get('qqNumber', '')
    weixin = request.POST.get('weixinNumber', '')
    mobile = request.POST.get('phoneNumber', '')
    q = Account.objects.filter(account=account)
    res = {"success":True,"err":None}
    if q :
        res["success"] = False
        res["err"] = "用户名重复"
    else:
        newAccount=Account(account=account,password=password,mail=mail,qqNumber=qq,weixinNumber=weixin,phoneNumber=mobile)
        newAccount.save()
    return  HttpResponse(json.dumps(res),content_type="application/json")

def getSession(request):
    name = request.GET.get('name','empty')
    name = getattr(request.session['user'],name)
    userid = getattr(request.session['user'],'id')
    return HttpResponse(json.dumps({'name':name,'id':userid}))