'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from bsite.models import User
from django.shortcuts import render


def index (request):
    return render_to_response('baraboo.html')

def investmentspage(request):
    return render_to_response('investments.html')

def loginpage(request):

    username = request.GET['username']
    password = request.GET['password']
    url = True
    dbuser = None
    print(username + " " + password)

    try:
        #Hacer select a base de datos
        dbuser = User.objects.get(userName = username)
        #-----------------------#
        #if dbuser.password == password:
        if url:
            return HttpResponseRedirect('investments.html')
        else:
            return render(request, 'baraboo.html',{'error': True})
    except:
        return HttpResponseRedirect('baraboo.html')
        
def formview(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        birthDate = request.POST.get('birthDate')
        country = request.POST.get('country')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        passwordConfirmation = request.POST.get('passwordConfirmation')

        #database select to login