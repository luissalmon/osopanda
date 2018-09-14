'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
=======
from django.shortcuts import render_to_response, render
>>>>>>> ethWalletReader

from bsite.models import User, Person

from django.http import HttpResponse

#from bsite.models import cuentaPrueba

from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider

from pprint import pprint

import binascii

def index (request):
    return render(request,'baraboo.html')

def homepage(request):
<<<<<<< HEAD
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

def hola (request):
    
    #TODO:Funcion Treaer bloque de wallets transacciones cumulativas DONE
    #TODO:Leer artículo DONE
    #TODO:PReguntar en el chat, investigar como obtener el numero de transaction hases between 2 wallets
    #TODO:
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    ethPrice = web3.eth.generateGasPrice()
    pprint(ethPrice)
    #Seleccionar cuenta de servidor
    cuentaBaraboo = web3.toChecksumAddress(web3.eth.accounts[0])
    balanceCuentaBaraboo = getAccountBalance(cuentaBaraboo,web3)
    #Seleccionar cuenta de cliente
    cuentaCliente = web3.toChecksumAddress(web3.eth.accounts[1])
    balanceCuentaCliente = getAccountBalance(cuentaCliente,web3)
    #Operación de depósito que retorna hash de la transacción
    TransactionHash1 = hacerTransaccion(cuentaCliente,cuentaBaraboo,10,web3)
    TransactionHash2 = hacerTransaccion(cuentaCliente,cuentaBaraboo,50,web3)
    TransactionHash3 = hacerTransaccion(cuentaCliente,cuentaBaraboo,100,web3)
    #Numero de transacciones que se hicieron
    NumeroTransacciones = web3.eth.getTransaction(TransactionHash3).blockNumber
    
    reciboTransaccion = web3.eth.getTransactionReceipt(TransactionHash3)
    
    pprint('Transferencia:')
    pprint(web3.eth.getTransactionByBlock(TransactionHash3,0))
    pprint(web3.eth.getTransactionByBlock(TransactionHash3,1))
    pprint(web3.eth.getTransactionByBlock(TransactionHash3,2))

    #hacer una funcion que pase ethereum de una cuenta a otra
    #ejecutar 2 veces
    #funcion que reciba 'to'
    #sacar el saldo de una transaccion (hash)
    #sacar la cantidad de ethereum que se ha mandado de un wallet a otro
    
    
    #web3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))    
    
    #web3 = Web3(HTTPProvider('https://mainnet.infura.io/metamask'))
    
    #web3 = Web3(HTTPProvider('https://127.0.0.1:8545'))
    
    #accId = 69
    #userAccounts = cuentaPrueba.objects.get(idCuenta=accId)    
    
    #apiKey = userAccounts.apiKey
    #apiSecret = userAccounts.apiSecret
    #provider = userAccounts.endpoint
    #cuentaNueva = web3.personal.newAccount('password')
    

    #lista_cuentas = web3.personal.listAccounts
    
    #depositWalletAdress = '0xf8438fF4cEB3b7465028CC3AaE11f9A147738223'
    
    #nblock = web3.eth.getBlock('latest')
    
    #numBloque = nblock['hash']
    #coinbase = web3.eth.coinbase
    
    #gasLimit = nblock.gasLimit
    #cuentaDef = web3.eth.defaultAccount
    #miningStatus = web3.eth.mining
    #hashRate = web3.eth.hashrate
    #gasPrice = web3.eth.gasPrice
   
    #checksumAcc = Web3.toChecksumAddress(depositWalletAdress)
    #balance = web3.eth.getBalance(checksumAcc)
    
        
    return render(request,'HolaMundo.html',{
        #'apiKey': apiKey,
        #'apiSecret' : apiSecret,
        ##'block':block,
        #'cuentaPersonal':lista_cuentas,
        #'nBlock':nblock,
        #'coinbase':coinbase,
        #'numBloque':numBloque,
        #'gasLimit':gasLimit,
        #'cuentaDef':cuentaDef,
        #'miningStatus':miningStatus,
        #'hashRate':hashRate,
        #'gasPrice':gasPrice,
        #'cuentas':cuentas,
        ##'balance':balance,
        #'nTransacciones':nTransacciones,
        #'hola':hola,
        ##'hashTransaccion':hashTransaccion,
        'balanceCuentaBaraboo':balanceCuentaBaraboo,
        'balanceCuentaCliente':balanceCuentaCliente,
        ##'splitedWord':splitedWord,
        'TransactionHash1':TransactionHash1,
        'TransactionHash2':TransactionHash2,
        'TransactionHash3':TransactionHash3,
        'NumeroTransacciones':NumeroTransacciones,
        'reciboTransaccion':reciboTransaccion
        #'accBalance':accBalance
    })


def hacerTransaccion(de,para,value,web3):
    hashT = binascii.hexlify(web3.eth.sendTransaction({'to':para,'from':de,'value':value}))
    return hashT.decode() 

def getAccountBalance(Account,web3):
    return web3.eth.getBalance(Account)
