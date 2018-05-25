from django.db import models
# Create your models here.
class Partner(models.Model):
    """
        合作伙伴
    """
    name           =    models.CharField('名称',max_length=100)
    phone_number   =    models.CharField('电话号码',max_length=100)
    charge_person  =    models.CharField('负责人',max_length=100)
    address        =    models.CharField('地址',max_length=200)

    supplier = "供应商"
    purchaser = "采购商"
    other = "其他"

    relative_types = (
                        ("供货商","供货商"),
                        ("采购商","采购商"),
                        ("其他","其他")
    )

    relative       =    models.CharField(max_length=100)
    goods          =    models.ManyToManyField('goods.Goods',blank=True)
    remark         =    models.TextField('remark',max_length=1000)