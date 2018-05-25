from django.conf.urls import url

from . import views
app_name = 'goods'
urlpatterns = [
    url(r'^create$',views.goodsCreate,name='goodsCreate'),
    url(r'^get',views.goodsGet,name='goodsGet'),
    url(r'^query',views.goodsQuery,name='goodsQuery'),
    url(r'^goodschanges/get',views.changesGet,name='changesGet'),
    url(r'^goodschanges/create',views.goodschangeCreate,name='goodschangeCreate'),
    url(r'^outgoodschanges/create',views.outgGoodschangeCreate,name='outGoodschangeCreate'),
]