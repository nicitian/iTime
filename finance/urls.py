from django.conf.urls import url

from . import views
app_name = 'finance'
urlpatterns = [
    url(r'^edit',views.EditFinance,name='EditFinance'),
    url(r'^get',views.GetFinance,name='GetFinance'),
    url(r'^financerecords/get',views.GetFinanceRecords,name='GetFinanceRecords')

]