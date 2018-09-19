from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('investments/', views.loadprojects, name="projects"),
    path('investments/<projectname>/', views.gotoproject, name="gotoproject"),
    path('page6/', views.page6, name="page6"),

    #Urls login/logout and register
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # Urls para recuperar cuenta y contraseña
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('recoverpassword/', views.recoverpassword, name="recover"),

    #Urls para confirmar cuenta
    path('confirm/', views.confirm, name="confirm"),
    path('sendConfirmation/', views.confirmAccount, name="send confirm")
]

