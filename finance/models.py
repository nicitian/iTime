from django.db import models

# Create your models here.
class Finance(models.Model):
    total_finance = models.IntegerField(default=0)
    total_income = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)

class FinanceRecords(models.Model):#财务记录
    create_time = models.DateTimeField("create time", auto_now=True)

    INCOME = '收入'
    COST = '支出'
    FinanC = '财务修改'
    op_types = (
        (COST,'支出'),
        (INCOME,'收入'),
        (FinanC,'财务修改')
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
            self.to.save()
        elif self.opration_type == '支出':
            self.to.total_cost = self.to.total_cost + self.money
            self.to.total_finance = self.to.total_finance - self.money
            self.to.save()
        super(FinanceRecords, self).save(*args, **kwargs)