'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.shortcuts import render_to_response

from django.contrib import auth

def index (request):
    return render_to_response('baraboo.html')

def vista_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password) 
    
    if user is not None and user.is_active:
        # Contraseña correcta y usuario marcado como "activo"
        auth.login(request, user)
        # Redireccciona a una página de entrada correcta.
        return HttpResponseRedirect("/account/loggedin/") 
    else:
        # Muestra una página de error
        return HttpResponseRedirect("/account/invalid/")