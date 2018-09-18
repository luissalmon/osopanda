from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name="login"),
    path('register/', views.register, name="register"),
    path('investments/', views.projects, name="projects"),
    path('page6/', views.page6, name="page6"),
    path('logout/', views.logoutUser, name="logout"),

    # Urls de prueba para recuperar cuenta y contraseña
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('recoverpassword/', views.recoverpassword, name="recover"),

    #Urls de prueba para confirmar cuenta
    path('confirm/', views.confirm, name="confirm"),
    path('sendConfirmation/', views.confirmAccount, name="send confirm")
]

