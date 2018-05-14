from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Questions
import json
# Create your views here.
def createQuestions(request):
    name = request.POST.get("name",None)
    type = request.POST.get('type',None)
    content = request.POST.get('content',None)
    if  Questions.objects.filter(name=name).first() is None:
        q = Questions(name=name,content=content,type=type)
        q.save()
        return HttpResponseRedirect("/login/questionmanager")
    else:
        return HttpResponseRedirect("/login/newquestion?err=True",{"err":True})

def showEditQuestions(request):
    id = request.GET.get("q_id",-1)
    id = int(id)
    q=Questions.objects.filter(pk=id).first()
    print("show edit q id :",q.id)
    if q:
        return render(request,'EditQuestion.html',{'question':q})
    else:
        return HttpResponseRedirect('/login/questionmanager')

def editQuestions(request):
    id = int(request.POST.get("q_id",'-1'))
    print('id=',id)
    info = {'name':request.POST.get("name","errname"),
            'type':request.POST.get("type","errtype"),
            'content':request.POST.get("content","errcontent")}
    print(Questions.objects.filter(pk=id))
    Questions.objects.filter(id=id).update(name=info['name'],type=info['type'],content=info['content'])
    return HttpResponseRedirect('/login/questionmanager')

def getQuestions(request):
    qs = Questions.objects.all()
    res = []
    for q in qs:
        res.append({'name':q.name,'type':q.type,'id':q.id,'content':q.content})
    return HttpResponse(json.dumps(res),content_type="application/json")