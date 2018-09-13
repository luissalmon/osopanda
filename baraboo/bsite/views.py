'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext


def index (request):
    return render_to_response('baraboo.html')

def investmentspage(request):
    return render_to_response('investments.html')

def loginpage(request):

    username = request.GET['username']
    password = request.GET['password']
    url = None
    dbuser = None
    print(username + " " + password)

    #Hacer select a base de datos
    
    #-----------------------#
    if username == 'luis' and password == '123':
        return HttpResponseRedirect('investments.html')
    else:
        return render(request, 'baraboo.html',{'error': True})
        

    
    # if user is not None and user.is_active:
    #     print('authenticated')
    #     # Contraseña correcta y usuario marcado como "activo"
    #     auth.login(request, user)
    #     # Redireccciona a una página de entrada correcta.
    #     return HttpResponseRedirect("investments.html")
    #     #return render_to_response('investments.html')
    # else:
    #     print('not authenticated')
    #     # Muestra una página de error
    #     return HttpResponseRedirect("investments.html")

def formulario(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        
        #database select to login