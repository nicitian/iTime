from django.db import models

# Create your models here.
class Account(models.Model):

    account = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)
    phoneNumber = models.CharField(max_length=100,null=True)
    qqNumber = models.CharField(max_length=100,null=True)
    weixinNumber = models.CharField(max_length=100,null=True)
    mail = models.EmailField(null=True)


class Questions(models.Model):
    name = models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=100,null=False)
    content = models.CharField(max_length=10000,null=False)