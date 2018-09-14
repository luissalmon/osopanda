'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

from bsite.models import User, Person

def index (request):
    return render(request,'baraboo.html')

def homepage(request):
    return render(request,'homepage.html')

def investments(request):
    return render(request, 'investments.html')



def loginpage(request):

    username = request.GET['username']
    password = request.GET['password']

    try:
        db = User.objects.get(userName = username)

        if db.password == password:
            return HttpResponseRedirect('homepage')
        else:   
            return render(request,'baraboo.html')
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

        birthDate = dobyear + "-" + dobmonth + "-" + dobday
        person = Person(name=name, lastName=lastName, birthDate=birthDate, mail=email)
        person.save()
        user = User(userName=username, password=password, idPerson=person)
        user.save()

    return HttpResponseRedirect('homepage')