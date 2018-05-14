from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Goods,GoodsChanges
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.models import Account
import json
from finance.models import Finance,FinanceRecords
# Create your views here.
def GetFinance(request):
    try:
        id = int(request.POST.get('id',1))
        finance = Finance.objects.get(id=id)
        body = {'finance':finance.total_finance,'income':finance.total_income,'cost':finance.total_cost}
    except:
        body={'finance':0,'income':0,'cost':0}
    res={'success':True,'body':body}
    return HttpResponse(json.dumps(res), content_type="application/json")

def createFinanceRecords(uid=1,fid=1,remark='',money=0,op_type='收入',re_type='其他'):
    user = Account.objects.get(id=uid)
    fi = Finance.objects.get(id=fid)
    new_fr = FinanceRecords(opration_type=op_type,money=money,remark=remark,to=fi,change_people=user,reason_choice=re_type)
    new_fr.save()

def EditFinance(request):
    finance = int(request.POST.get('finance', 0))
    op_type = request.POST.get('type', 0)
    id = int(request.POST.get('userid', 1))
    fid = int(request.POST.get('fid',1))
    reason = request.POST.get('reason',' ')
    modifyer = Account.objects.get(id=id)
    if not Finance.objects.all():
        new_finance = Finance(total_cost=0,total_finance=0,total_income=0)
        new_finance.save()
        remark = reason
        new_FR = FinanceRecords(money=finance,change_people=modifyer,remark=remark,to=new_finance,opration_type=op_type,reason_choice='其他')
        new_FR.save()
    else:
        f = Finance.objects.get(id=fid)
        remark = reason
        new_FR = FinanceRecords(money=finance,change_people=modifyer, remark=remark, to=f, opration_type=op_type,reason_choice='其他')
        new_FR.save()
    res = {"success": True, "err": None}
    return HttpResponse(json.dumps(res), content_type="application/json")

def GetFinanceRecords(request):
    FRs = FinanceRecords.objects.all()#FR 表示finance records 的缩写
    # goodOuts = OutGoodsChanges.objects.all()
    # goodRes = goodIns |goodOuts
    FRres = FRs
    FRres = FRres.order_by('-create_time')
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size', 10))
    apiUrl = ''.join(['localhost:8000', '/finance/financerecords/get'])
    total = FRs.count()
    if page == 'max':
        page = total / size
    # print(request.META)
    if FRres:
        paginator = Paginator(FRres, size)  # Show 25 contacts per page
        FR = [
                {
                    'money':fr.money,
                    'change_people':fr.change_people.account,
                    'remark':fr.remark,
                    'op_type':fr.opration_type,
                    're_type':fr.reason_choice,
                    'datetime':fr.create_time.strftime("%Y-%m-%d %H:%M:%S")
                } for fr in paginator.page(page)
        ]
        res = {
                "body": FR,
                "pageinfo": {
                                'total': total,
                                'current': page,
                                'size': size,
                                "apiUrl": apiUrl
                            }
        }
        return HttpResponse(json.dumps(res), content_type="application/json")
        # try:
        #     goods = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     goods = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     goods = paginator.page(paginator.num_pages)
    else:
        res = {"body": [], "pageinfo": {'total': total, 'crrent': page, 'size': size, "apiUrl": apiUrl}}
        return HttpResponse(json.dumps([]), content_type="application/json")