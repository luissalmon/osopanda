from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name="login"),
    path('register/', views.formview, name="register"),
    # path('login/homepage/', views.homepage, name="homepage"),
    # path('login/homepage/<username>/', views.homepage, name="homepage"),    
    # path('login/homepage/<username>/investments/', views.projects, name="gotoprojects"),
    path('investments/', views.projects, name="projects")
    #path('adios/', views.hola, name= 'holamundo')
]

