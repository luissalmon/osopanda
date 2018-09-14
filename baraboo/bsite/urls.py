from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name="login"),
    path('register/', views.formview, name="register"),
    path('login/homepage.html', views.homepage, name = 'homepage')
]