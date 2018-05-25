from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Finance(models.Model):
    total_finance = models.IntegerField(default=0)
    total_income = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)


class FinanceMonth(models.Model):#财务月账单
    opt = models.CharField(max_length=100,default='所有')
    typ = models.CharField(max_length=100,default='所有')
    total_finance = models.IntegerField(default=0)
    total_income = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
    year_month = models.IntegerField(blank=False,null=False)
    to_finance = models.ForeignKey('Finance')# 关联到财务现状
    partner = models.ForeignKey('partner.partner',blank=True,null=True)





class FinanceRecords(models.Model):#财务记录
    create_time = models.DateTimeField("create time",default=timezone.now)
    partner = models.ForeignKey('partner.partner', blank=True,null=True)

    INCOME = '收入'
    COST = '支出'

    op_types = (
        (COST,'支出'),
        (INCOME,'收入'),
    )

    opration_type = models.CharField(choices=op_types, default=INCOME, max_length=100)

    putin = '入库'
    putout = '出库'
    other = '其他'
    re_types = (
        (putin, '入库'),
        (putout, '出库'),
        (other, '其他'),
    )

    reason_choice = models.CharField(choices=re_types, default=other, max_length=100)

    money = models.IntegerField(default=0)
    to = models.ForeignKey('Finance')  # 关联到财务现状
    change_people = models.ForeignKey('login.Account')  # 修改人员
    remark = models.CharField(default="其他",max_length=200)#备注

    def save(self,*args,**kwargs):

        if self.opration_type == '收入':
            self.to.total_income  = self.to.total_income + self.money
            self.to.total_finance = self.to.total_finance + self.money
            income = self.money
            cost = 0
            self.to.save()
        elif self.opration_type == '支出':
            self.to.total_cost = self.to.total_cost + self.money
            self.to.total_finance = self.to.total_finance - self.money
            income = 0
            cost = self.money
            self.to.save()
        super(FinanceRecords, self).save(*args, **kwargs)

        year_month = int(self.create_time.strftime("%Y%m"))


        def createFM(year_month,opt,typ,to_finance):

            DFM = FinanceMonth.objects.get_or_create(year_month=year_month,opt=opt,typ=typ,to_finance=to_finance)[0]
            DFM.total_finance = DFM.total_finance + income - cost
            DFM.total_income += income
            DFM.total_cost += cost
            DFM.save()

        createFM(year_month=year_month,opt=self.opration_type,typ=self.reason_choice,to_finance=self.to)
        createFM(year_month=year_month,opt=self.opration_type,typ='所有',to_finance=self.to)
        createFM(year_month=year_month, opt='所有', typ=self.reason_choice, to_finance=self.to)
        createFM(year_month=year_month, opt='所有', typ='所有', to_finance=self.to)





