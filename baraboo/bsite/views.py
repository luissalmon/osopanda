'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

<<<<<<< HEAD
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
=======
from django.shortcuts import render_to_response, HttpResponseRedirect

>>>>>>> 0bc44a63bb1c0b3c064c12f678288e81947d1f3b
from django.contrib import auth
from bsite.forms import Person_Form

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
        url = "investments.html"
        return HttpResponseRedirect(url)
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

def vistaFormulario(request):
    if request.method == 'POST':
        form = Person_Form(request.POST)
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        #database select to login