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

    try:
        #Hacer select a base de datos
        dbuser = User.objects.get(userName = username)
        #-----------------------#
        if dbuser.password == password:
            return HttpResponseRedirect('investments.html')
        else:
            return render(request, 'baraboo.html',{'error': True})
    except:
        return HttpResponseRedirect('/')
        
def formview(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        dobday = request.POST.get('dobday')
        dobmonth = request.POST.get('dobmonth')
        dobyear = request.POST.get('dobyear')
        country = request.POST.get('country')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConfirmation = request.POST.get('passwordConfirmation')

    return render(request, 'investments.html')
        #database select to login