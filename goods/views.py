from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Goods,GoodsChanges
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.models import Account
from finance.views import createFinanceRecords as createFr
import json
# Create your views here.
def goodsCreate(request):
    print(request.POST)
    name = request.POST.get('name',None)
    goodsQuery = Goods.objects.filter(name=name)
    if goodsQuery :
        res = {"success":False,"err":"商品名字重复"}
    else:
        res = {"success": True, "err": None}
        costprice = float(request.POST.get('costprice',0))
        saleprice = float(request.POST.get('saleprice', 0))
        initotal = int(request.POST.get('initotal', 0))
        desc = request.POST.get('desc','')
        goods = Goods(name=name,costprice=costprice,saleprice=saleprice,initotal=initotal,desc=desc)
        goods.save()
    return HttpResponse(json.dumps(res),content_type="application/json")

def goodsGet(request):
    print(request.session['user'].account)
    goods_list = Goods.objects.all()
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size',10))
    apiUrl = ''.join(['localhost:8000','/goods/get'])
    total = Goods.objects.count()
    if page == 'max':
        page = total/size
    # print(request.META)
    if goods_list:

        paginator = Paginator(goods_list, size)  # Show 25 contacts per page

        goods = [ {"name":good.name,"costprice":good.costprice,"saleprice":good.saleprice,"initotal":good.initotal,"desc":good.desc,"id":good.id} for good in paginator.page(page)]
        res = {"body":goods,"pageinfo":{'total':total,'current':page,'size':size,"apiUrl":apiUrl}}
        return HttpResponse(json.dumps(res),content_type="application/json")
        # try:
        #     goods = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     goods = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     goods = paginator.page(paginator.num_pages)
    else:
        res = {"body": [], "pageinfo": {'total': total, 'crrent': page, 'size': size,"apiUrl":apiUrl}}
        return HttpResponse(json.dumps([]),content_type="application/json")

def changesGet(request):

    goodIns = GoodsChanges.objects.all()
    # goodOuts = OutGoodsChanges.objects.all()
    # goodRes = goodIns |goodOuts
    goodRes = goodIns
    goodRes = goodRes.order_by('-create_time')
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size',10))
    apiUrl = ''.join(['localhost:8000','/goods/get'])
    total = goodIns.count()
    if page == 'max':
        page = total/size
    # print(request.META)
    if goodRes:

        paginator = Paginator(goodRes, size)  # Show 25 contacts per page

        goods = [ {"opration":change.opration_type,"name":change.to.name,"price":change.price,"datetime":change.create_time.strftime("%Y-%m-%d %H:%M:%S"),"totalprice":change.total_price(),'count':change.count} for change in paginator.page(page)]
        res = {"body":goods,"pageinfo":{'total':total,'current':page,'size':size,"apiUrl":apiUrl}}
        return HttpResponse(json.dumps(res),content_type="application/json")
        # try:
        #     goods = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     goods = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     goods = paginator.page(paginator.num_pages)
    else:
        res = {"body": [], "pageinfo": {'total': total, 'crrent': page, 'size': size,"apiUrl":apiUrl}}
        return HttpResponse(json.dumps([]),content_type="application/json")

def goodschangeCreate(request):

    goodsid = request.GET.get('goodsid',False)
    uid = request.GET.get('userid',1)
    price = request.GET.get('price',0)
    count = request.GET.get('count',0)
    op_type = request.GET.get('type','入库')
    if goodsid:
        goodsid = int(goodsid)
        Uid = int(uid)
        count = int(count)
        price = int(price)

        goods = Goods.objects.get(id=goodsid)
        price = goods.costprice if op_type == '入库' else goods.saleprice
        change_people = Account.objects.get(pk=Uid)
        print(goods)
        print(change_people)
        goodschange = GoodsChanges(change_people=change_people,count=count,to=goods,price=price,opration_type=op_type)
        goodschange.save()
        op_t = '支出' if op_type=='入库' else '收入'
        money = count*goods.costprice if op_t == '支出' else count*goods.saleprice
        createFr(uid=Uid,money=money,op_type=op_t,re_type=op_type,remark="\"{0}\"{1}{2}（单位）".format(goods.name,op_type,count))
        res={"success":True,"error":None}
        return HttpResponse(json.dumps([res]), content_type="application/json")
    else:
        res = {"success": False, "error": "params error"}
        return HttpResponse(json.dumps([res]), content_type="application/json")

def outgGoodschangeCreate(request):

    goodsid = request.GET.get('goodsid',False)
    uid = request.GET.get('userid',1)
    price = request.GET.get('price',0)
    count = request.GET.get('count',0)

    if goodsid:
        goodsid = int(goodsid)
        Uid = int(uid)
        count = int(count)
        price = int(price)

        goods = Goods.objects.get(id=goodsid)
        change_people = Account.objects.get(pk=Uid)



        res={"success":True,"error":None}
        return HttpResponse(json.dumps([res]), content_type="application/json")
    else:
        res = {"success": False, "error": "params error"}
        return HttpResponse(json.dumps([res]), content_type="application/json")