from django.shortcuts import render
from .models import Partner
import json
from django.http import HttpResponse
from goods.models import Goods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def partnerQuery(request):

    name = request.GET.get('name','')
    qs = Partner.objects.filter(name__contains=name)
    res = [{'value':g.name,'id':g.id} for g in qs]
    return HttpResponse(json.dumps(res),content_type="application/json")

def PartnerCreate(request):
    print('partner create post is:',request.POST)
    name = request.POST.get('name', None)
    querys = Partner.objects.filter(name=name)
    if querys:
        res = {"success": False, "err": "名字重复"}
    else:
        res = {"success": True, "err": None}
        address = request.POST.get('address')
        relation = request.POST.get('relation')
        print('goods in post is:',request.POST.get('goods',[]))
        goods_ids = request.POST.get('goods','')
        if goods_ids:
            goods = [int(g) for g in goods_ids.split(',')]
        else:
            goods = []
        print('goods is :',goods)
        charge_person = request.POST.get('charge_person','')
        remark = request.POST.get('remark')
        phone_number = request.POST.get('phone_number','')

        querys = Partner(name=name,address=address,relative=relation,charge_person=charge_person,phone_number=phone_number,remark=remark)
        querys.save()
        for g in goods:
            querys.goods.add(Goods.objects.get(pk=g))
        querys.save()
    return HttpResponse(json.dumps(res), content_type="application/json")

def partnerGet(request):

    query_list = Partner.objects.all()
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size',10))
    apiUrl = ''.join(['localhost:8000','/partner/get'])
    total = Partner.objects.count()
    if page == 'max':
        page = total/size
    # print(request.META)
    if query_list:

        paginator = Paginator(query_list, size)  # Show 25 contacts per page

        qs = [
                    {
                        "name":p.name,
                        "charge_person":p.charge_person,
                        "address":p.address,
                        "goods":','.join([g.name for g in p.goods.all()]),
                        "remark":p.remark,
                        "phone_number":p.phone_number,
                        "relative":p.relative
                        } for p in paginator.page(page)]
        res = {"body":qs,"pageinfo":{'total':total,'current':page,'size':size,"apiUrl":apiUrl}}
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
