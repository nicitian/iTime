from django.conf.urls import url

from . import views
app_name = 'login'
urlpatterns = [
    url(r'^$',views.showLoginPage,name='loginPage'),
    url(r'^toRegister$',views.showRegisterPage,name='showRegisterPage'),
    url(r'^toRegister_$',views.showRegisterPage_,name='showRegisterPage'),
    url(r'^Regist$',views.Regist,name='Regist'),
    url(r'^Regist_$',views.RegistApi,name='Regist_'),
    url(r'^isRegisted$',views.isRegisted,name='isRegisted'),
    url(r'^sumbit$',views.submit,name='submit'),
    url(r'^getUser$',views.getUser,name='getUser'),
    url(r'^updateUser$',views.updateUser,name='updateUser'),
    url(r'^index$',views.index,name='index'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^questionmanager$',views.questionmanager,name='questionmanager'),
    url(r'^newquestion$',views.newQuestion,name='newQuestion'),
    url(r'^getS$',views.getSession,name='getSession'),

]