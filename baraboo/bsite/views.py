'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from bsite.models import Person, User, PresentationProjectData, PresentationProjectImage, ImageType
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from bsite import PresentationProject, job

def page6(request):
    return render(request,'page6.html')

def index (request):
    isLogged = False
    #job.job()
    if request.user.id:
        isLogged = True
    return render(request,'baraboo.html', {'isLogged':isLogged, 'username': request.user.username})

def userprofile(request):
    return render(request,'userprofile.html', {'username' : request.user.username})

#------------------
class project():
    Name = ""
    Location = ""
    Time = ""
    FinancialReturn = ""
    RisedMoney = ""
    MaximumAmount = ""
#------------------

def loadprojects(request):

    isLogged = False
    if request.user.id:
        isLogged = True

    proj = project()
    proj.Name = "Urbane"
    proj.Location = "San Pedro"
    proj.Time = "2 years"
    proj.FinancialReturn = "10%"
    proj.RisedMoney = "500,000"
    proj.MaximumAmount = "3,000,000"

    projects = []
    projects.append(proj)

    return render(request, 'investments.html', {'projects':projects, 'isLogged':isLogged, 'username': request.user.username})

#def gotoproject(request, projectname):
def gotoproject(request):
    #Get all the info about the project


    return render(request, 'project.html')

#------------------------------------------
def loginUser(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = authenticate(request, username = username, password = password)
        login(request, user)
        if user:
            if user.confirm == False:
                logout(request)
                return HttpResponseRedirect('/confirm/')

            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

def logoutUser(request):
    logout(request)

    return HttpResponseRedirect('/')
        
def register(request):
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
        
        try:
            birthDate = dobyear + "-" + dobmonth + "-" + dobday
            person = Person(name=name, lastName=lastName, birthDate=birthDate, mail=email, country=country)
            code = get_random_string(length=32)

            if person:
                person.save()
                User.objects.create_user(username, password, person, code)

                emailMessage = "Your confirmation code is: " + code
                send_mail('Confirm your account',
                    emailMessage,
                    'gregorio.garza.garcia@gmail.com',
                    [email],
                    fail_silently=False)
        except:
            return HttpResponseRedirect('/')
        
        return HttpResponseRedirect('/')

def forgotpassword(request):
    if request.user.id:
        return HttpResponseRedirect('/')
    return render(request, 'forgotpassword.html')

def recoverpassword(request):
    email = request.POST.get('email')
            
    try:
        person = Person.objects.get(mail = email)
        if person:
            user = User.objects.get(idPerson = person.idPerson)
            newpassword = User.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            emailMessage = "Username: " + user.username + "\n" + "Password: " + newpassword
        
            send_mail('Recover Password',
                emailMessage,
                'gregorio.garza.garcia@gmail.com',
                [email],
                fail_silently=False)
            user.set_password(newpassword)
            user.save() 
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

def getPresentationProject(request, id):
    pp = PresentationProject()

    #Get the model base on Id to create content to show
    modelpp = PresentationProjectData.objects.get(idProject = id)
    
    #Get the id's of images for the presentation section 
    imgToPresentationIds = ImageType.objects.filter(idImageType = 1)
    imgToGalletyIds = ImageType.objects.filter(idImageType = 2)

    #y
    imgToPresentation = PresentationProjectImage.filter(
        idPresentationProjectData__in=modelpp.idpresentationProjectData).filter(
            idImageType__in=imgToPresentationIds)

    imgToGallery = PresentationProjectImage.filter(
        idPresentationProjectData__in=modelpp.idpresentationProjectData).filter(
            idImageType__in=imgToGalletyIds)

    pp.idProject = id
    pp.tittle = modelpp.tittle
    pp.description = modelpp.description
    pp.returnOfInversion = modelpp.returnOfInversion
    pp.expirationDate = modelpp.expirationDate
    pp.initialInvestmentRound = modelpp.initialInvestmentRound
    pp.taretCapital = modelpp.taretCapital
    pp.video = modelpp.video
    pp.presentation = imgToPresentation
    pp.images = imgToGallery

    return render(request, 'pantalla6.html', {'pp':pp})

def confirm(request):
    if request.user.id:
        return HttpResponseRedirect('/')
    return render(request, 'confirmAccount.html')

def confirmAccount(request):
    code = request.POST.get('code')

    user = User.objects.get(confirmationCode = code)
    if user:
        user.confirm = True
        user.save()

    return HttpResponseRedirect('/')

def getUserDataFromKYC():

    updateUserAfterKYC()
    updateWalletAfterKYC()
    return 1

def updateUserAfterKYC():

    return 1

def updateWalletAfterKYC():

    return 1

def changeKycStatusForPendientUsers():
    #funcion periodica
    #getPendientUsers()
    return 1

def insertUserToWhiteList():
    getWalletUser()

    return 1


def getWalletUser(request):
    #idUser = request.iduser
    #walletAddre
    return HttpResponseRedirect('/')

def getTokenBalance():
    return 1