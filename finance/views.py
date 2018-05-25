from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Goods,GoodsChanges
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.models import Account
import json
from finance.models import Finance,FinanceRecords,FinanceMonth
from django.db.models import Sum
from partner.models import Partner
# Create your views here.
def GetFinance(request):
    print(request.GET)
    if request.GET.get('isquery',False) in ['',False]:
        try:
            id = int(request.GET.get('id',1))
            finance = Finance.objects.get(id=id)
            body = {'finance':finance.total_finance,'income':finance.total_income,'cost':finance.total_cost}
        except:
            body={'finance':0,'income':0,'cost':0}
    else:
        start_gte = request.GET.get('str_start_date_gte','')
        start_lt = request.GET.get('str_start_date_lt','')

        start_year_month = int(request.GET.get('start_year_month','201801'))
        end_year_month = int(request.GET.get('end_year_month','210001'))

        end_gte = request.GET.get('str_end_date_gte','')
        end_lte = request.GET.get('str_end_date_lte','')

        typ = request.GET.get('type','')
        opt = request.GET.get('opt','')
        FM = FinanceMonth.objects.all()
        FR = FinanceRecords.objects.all()

        if typ not in ['','所有']:
            FM = FM.filter(typ=typ)
            FR = FR.filter(reason_choice=typ)
        else:
            FM = FM.filter(typ='所有')

        if opt not in ['','所有']:
            FM = FM.filter(opt=opt)
            FR = FR.filter(opration_type=opt)
        else:
            FM = FM.filter(opt='所有')

        num_start = 1
        num_end = 0

        if start_gte and end_lte:
            nums = start_gte.split('-')
            num_start = int(nums[0])*100+int(nums[1])
            nums = end_lte.split('-')
            num_end = int(nums[0])*100+int(nums[1])
        print("num_start:",num_start,",num_end:",num_end)

        print("start_begin={0},start_end={1},end_begin{2}=,end_end{3}".format(start_gte,start_lt,end_gte,end_lte))
        times = 1
        print("FR.count()=", FR.count(),times)
        times += 1
        if num_start == num_end:
            print('start==end')
            FR = FR.filter(create_time__gte=start_gte,create_time__lte=end_lte)
        else:
            print('start!=end')
            FR1 = FR
            FR2 = FR

            if start_gte:
                FR1 =FR.filter(create_time__gte=start_gte,create_time__lt=start_lt)
            else:
                FR1 = FR.filter(create_time='2000-01-01')

            if end_gte:
                FR2 = FR.filter(create_time__gte=end_gte,create_time__lte=end_lte)
            else:
                FR2 = FR.filter(create_time='2000-01-01')

            FR=FR1|FR2
            FR.distinct()


        if start_year_month:
            FM = FM.filter(year_month__gt=start_year_month,year_month__lt=end_year_month)
        if FM:
            FMd = FM.aggregate(Sum('total_finance'),Sum('total_cost'),Sum('total_income'))
        else:
            FMd = {
                'total_finance__sum':0,
                'total_income__sum':0,
                'total_cost__sum':0
            }
        print("fmd=",FMd)
        print("FR.count()=",FR.count())
        FR_income = FR.filter(opration_type='收入').aggregate(Sum('money')) if FR.filter(opration_type='收入').aggregate(Sum('money'))['money__sum'] else {'money__sum':0}
        print('FR_income=',FR_income)
        FR_cost = FR.filter(opration_type='支出').aggregate(Sum('money')) if FR.filter(opration_type='支出').aggregate(Sum('money'))['money__sum'] else {'money__sum':0}
        FR_finance = FR_income['money__sum'] - FR_cost['money__sum']
        print('fr_income=',FR_income,'  fr_cost=',FR_cost,'  fr_finance',FR_finance)
        body = {
                'finance':FMd['total_finance__sum']+FR_finance,
                'income':FMd['total_income__sum']+FR_income['money__sum'],
                'cost':FMd['total_cost__sum']+FR_cost['money__sum']
        }
    res={'success':True,'body':body}
    return HttpResponse(json.dumps(res), content_type="application/json")

def createFinanceRecords(uid=1,fid=1,remark='',money=0,op_type='收入',re_type='其他',partner=''):
    user = Account.objects.get(id=uid)
    fi = Finance.objects.get(id=fid)
    new_fr = FinanceRecords(opration_type=op_type,money=money,remark=remark,to=fi,change_people=user,reason_choice=re_type)
    if partner:
        new_fr.partner = partner
    new_fr.save()

def test_gen_all_FR(request):
    allFRS = FinanceRecords.objects.all()
    for fr in allFRS:
        fr.save()
    res=['ok']
    return HttpResponse(json.dumps(res), content_type="application/json")
def EditFinance(request):
    finance = int(request.POST.get('finance', 0))
    op_type = request.POST.get('type', 0)
    id = int(request.POST.get('userid', 1))
    fid = int(request.POST.get('fid',1))
    reason = request.POST.get('reason',' ')
    partner = request.POST.get('partner')
    modifyer = Account.objects.get(id=id)
    if not Finance.objects.all():#第一次创建则自动创建一个finance
        new_finance = Finance(total_cost=0,total_finance=0,total_income=0)
        new_finance.save()
        remark = reason
        new_FR = FinanceRecords(money=finance,change_people=modifyer,remark=remark,to=new_finance,opration_type=op_type,reason_choice='其他')
        new_FR.save()
    else:
        f = Finance.objects.get(id=fid)
        remark = reason

        new_FR = FinanceRecords(money=finance,change_people=modifyer, remark=remark, to=f, opration_type=op_type,reason_choice='其他')
        if partner:
            partner = Partner.objects.get(id=int(partner))
            new_FR.partner = partner
        new_FR.save()
    res = {"success": True, "err": None}
    return HttpResponse(json.dumps(res), content_type="application/json")

def GetFinanceRecords(request):

    is_query = request.GET.get('isquery', False)
    if not is_query:
        FRs = FinanceRecords.objects.all()#FR 表示finance records 的缩写
    else:
        rget = request.GET.get
        FRs = FinanceRecords.objects.all()
        startdate = rget('startdate',False)
        if startdate not in ['',False]:
            startdate = '{0} 00:00'.format(startdate)

            FRs = FRs.filter(create_time__gte=startdate)
        enddate = rget('enddate', False)
        if enddate not in ['',False]:
            enddate = '{0} 00:00'.format(enddate)

            FRs = FRs.filter(create_time__lte=enddate)
        typ = rget('type', False)
        if typ not in ['','所有']:
            FRs = FRs.filter(reason_choice=typ)
        opt = rget('opt', False)
        if opt not in ['','所有']:
            FRs = FRs.filter(opration_type=opt)
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
                    'partner': fr.partner.name if fr.partner else '',
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