from django.conf.urls import url

from . import views
app_name = 'questions'
urlpatterns = [
    url(r'^create$',views.createQuestions,name='createQuestions'),
    url(r'^show/edit$',views.showEditQuestions,name='showEditQuestions'),
    url(r'^edit$', views.editQuestions, name='editQuestions'),
    url(r'^get$', views.getQuestions, name='getQuestions')

]