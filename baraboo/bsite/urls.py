from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.vista_login, name = 'login')
    #url(r'', LoginView.as_view(template_name="baraboo.html"), name="login")

]