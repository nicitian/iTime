from django.conf.urls import url,include
from django.contrib import admin
from partner import views

urlpatterns = [
    url(r'^create$',views.PartnerCreate,name='PartnerCreate'),
    url(r'^get',views.partnerGet,name='partnerGet'),
    url(r'^query',views.partnerQuery,name='partnerQuery')
]
