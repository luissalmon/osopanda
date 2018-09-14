from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('login/investments.html', views.investmentspage, name = 'investments')
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name="login"),
    path('provisionalName', LoginView.as_view(template_name="baraboo2.html"), name="provisionalName"),
    path('register/', views.formview, name="register"),
]