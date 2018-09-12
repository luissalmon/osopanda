'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.shortcuts import render_to_response, render

from django.contrib import auth

from django.http import HttpResponse

from bsite.models import cuentaPrueba

from web3.auto import w3

from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider

def index (request):
    return render_to_response('baraboo.html')

def homepage(request):
    return render_to_response('registrar.html')


def hola (request):
    accId = 69
    
    
    web3 = Web3(WebsocketProvider('ws://127.0.0.1:8000'))    
    
    
    userAccounts = cuentaPrueba.objects.get(idCuenta=accId)
    
    apiKey = userAccounts.apiKey
    apiSecret = userAccounts.apiSecret
    provider = userAccounts.endpoint
    
    block = w3.eth.blockNumber()
    
    texto =  'llave normal: ' + apiKey + ' llave secreta: ' + apiSecret
    
    return render(request,'HolaMundo.html',{
        'apiKey': apiKey,
        'apiSecret' : apiSecret,
        'block':block
    })

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
