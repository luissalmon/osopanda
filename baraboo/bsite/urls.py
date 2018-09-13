from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    #path('', LoginView.as_view(template_name="baraboo.html"), name="login"),
    path('login/', views.loginpage, name="login"),
    path('register/', views.formview, name="register"),
    path('login/investments.html', views.investmentspage, name = 'investments')
]