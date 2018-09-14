from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    path('', LoginView.as_view(template_name="baraboo.html"), name="login"),
    path('provisionalName', LoginView.as_view(template_name="baraboo2.html"), name="provisionalName"),
    path('investments', LoginView.as_view(template_name="investments.html"), name="investments"),
    path('registrar', views.homepage, name = 'home')
]