from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class GoodsChanges(models.Model):

    price = models.FloatField(blank=True,default=0)#入库价格
    count = models.IntegerField(default=0)#入库数量
    old_total = models.IntegerField(default=0)#修改之前的库存

    IN = '入库'
    OUT = '出库'
    op_types = (
        (OUT,'出库'),
        (IN,'入库')
    )

    opration_type = models.CharField(choices=op_types,default=IN,max_length=100)
    to = models.ForeignKey('Goods')#关联到商品
    change_people = models.ForeignKey('login.Account')#修改人员
    create_time = models.DateTimeField("create time",auto_now=True)
    def new_total(self):
        return self.old_total+self.count

    def total_price(self):
        return self.count*self.price

    def save(self,*args,**kwargs):
        if self.opration_type == "入库":
            self.to.initotal = self.to.initotal + self.count
        else:
            self.to.initotal = self.to.initotal - self.count
        self.to.save()
        super(GoodsChanges,self).save(*args,**kwargs)


class Goods(models.Model):

    name = models.CharField(max_length=100,null=False)#商品名字
    costprice = models.FloatField(max_length=100,default=0)#进货价
    saleprice = models.FloatField(max_length=100,default=0)#售价
    initotal = models.FloatField(max_length=100,default=0)#库存
    desc = models.TextField(null=True)#商品描述
    create_user = models.OneToOneField('login.Account',null=True)  # 创建人员
    store = models.ForeignKey('StoreHouse',related_name='storehouse',blank=True,null=True)#存放的仓库


    # history = models.OneToman
class StoreHouse(models.Model):

    name = models.CharField(max_length=100,null=False)#仓库名字
    address = models.CharField(max_length=300,blank=True)#仓库地址
    area = models.IntegerField(blank=True)#仓库面积
    height = models.IntegerField(blank=True)#仓库共几楼