from django.db import models



class Questions(models.Model):
    name = models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=100,null=False)
    content = models.CharField(max_length=10000,null=False)