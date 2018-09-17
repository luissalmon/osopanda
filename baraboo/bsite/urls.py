from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name="login"),
    path('register/', views.register, name="register"),
    path('investments/', views.projects, name="projects"),
    path('logout/', views.logoutUser, name="logout"),

    # Urls de prueba para recuperar cuenta y contraseña
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('recoverpassword/', views.recoverpassword, name="recover")
]

