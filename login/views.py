from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from questions.models import Questions
import functools

import  json
# Create your views here.
from .models import Account

def dec_login(func):
    def wrapper(request,*args,**kw):
        if request.session.get("",False):
            pass
        return func(request,*args,**kw)
    return wrapper

def showLoginPage(request):
    return render(request,'login/login.html',{'ok':False})

def submit(request):
    print("----------------",request.POST)
    account = request.POST['account']
    password = request.POST['password']
    print(account,password)
    q = Account.objects.filter(account=account,password=password).first()
    if q:
        request.session['login'] = True
        request.session['user'] = q
        return HttpResponseRedirect('/login/index')
    else:
        return render(request,'login/login.html',{'err':True,'info':"账号或密码输入有误！！"})

def questionmanager(request):
    Qs = Questions.objects.all()
    print(Qs)
    if request.session.get('login',False):
        return render(request,'QuestionManager.html',{'user':request.session['user'],'pageContent':"查看内容",'questions':Qs})
    else:
        return render(request,'login/login.html',{'err':True})

def newQuestion(request):
    pageContent = "名字重复，请重新创建！" if request.GET.get('err','false')=='True' else "创建内容"
    if request.session.get('login',False):
        return render(request,'NewQuestion.html',{'user':request.session['user'],'pageContent':pageContent})
    else:
        return render(request,'login/login.html',{'err':True})

def index(request):
    # print(request.session.get('login',False))
    # print(request.session.get('user',False))
    if request.session.get('login',False):
        return render(request,'index_.html',{'user':request.session['user']})
    else:
        return render(request,'login/login.html',{'err':True,'info':"请先登录！！！"})

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
    q = Account.objects.filter(account=account)
    if q :
        return render(request,'register.html',{'repeatd':True})
    else:
        newAccount=Account(account=account,password=password)
        newAccount.save()
        return  render(request,'login/login.html',{'ok':True})

def RegistApi(request):
    print("---------------",request.POST)
    account = request.POST.get('account')
    password = request.POST.get('password')
    q = Account.objects.filter(account=account)
    res = {"success":True,"err":None}
    if q :
        res["success"] = False
        res["err"] = "用户名重复"
    else:
        newAccount=Account(account=account,password=password)
        newAccount.save()
    return  HttpResponse(json.dumps(res),content_type="application/json")

def getSession(request):
    name = request.GET.get('name','empty')
    name = getattr(request.session['user'],name)
    userid = getattr(request.session['user'],'id')
    return HttpResponse(json.dumps({'name':name,'id':userid}))