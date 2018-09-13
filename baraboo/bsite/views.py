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

#from bsite.models import DocumentType, Role, Person, User, UserRole, Wallet, KYCRequest, Document, PersonDocument


def index (request):
    # doct = DocumentType(name="INE", description="Identificacion oficial")
    # doct.save()

    # rol = Role(roleName="Inversionista", roleDescription="ejemplo")
    # rol.save()

    # per = Person(name="BDJGL", lastName="baraboo", birdDate="2018-02-05", mail="tata@tata.com")
    # per.save()

    # ptemp = Person.objects.get(idPerson=1)
    # u = User(userName="usuario", password="contraseña", idPerson=ptemp, active=1)
    # u.save()

    # utemp = User.objects.get(idUser=1)
    # roltemp = Role.objects.get(idRole=1)
    # ur = UserRole(idUser=utemp, idRole=roltemp)
    # ur.save()

    # wal = Wallet(idUser=utemp, address="")
    # wal.save()

    # kyc = KYCRequest(idUser=utemp)
    # kyc.save()

    # dttemp = DocumentType.objects.get(idDocumentType=1)
    # doc = Document(path="/Users/luis/Desktop/respaldo beto/Music/iTunes/iTunes Media/Music/Electric Guest/Mondo",
    #     idDocumentType=dttemp)
    # doc.save()

    # idctemp = Document.objects.get(idDocument=1)
    # pd = PersonDocument(idPerson=ptemp, idDocument=idctemp)
    # pd.save()
    return render_to_response('baraboo.html')

def investmentspage(request):
    return render_to_response('investments.html')

def loginpage(request):

    username = request.GET['username']
    password = request.GET['password']
    print(username + " " + password)
    url = False

    try:
        #Hacer select a base de datos
        #dbuser = User.objects.get(userName = username)
        #-----------------------#
        #if dbuser.password == password:
        if url:
            return HttpResponseRedirect('investments.html')
        else:
            return render(request, 'baraboo.html',{'error': True})
    except:
        return HttpResponseRedirect('/')
        
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

    return render(request, 'investmens.html')
        #database select to login