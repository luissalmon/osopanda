from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider

import binascii

#def getGraphInfo(usuario):
    #user = Person.objects.get(idUser = usuario)
    #wallet = Wallet.objects.get(idUser = user.idUser)
    #proyecto = PersonDocument.objects.get(idPerson = user.idUser)
    #walletTransactions = getWalletTransactions(wallet)

#función para traer todas las transacciones que hizo una wallet
def getWalletTransactions(from1):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    transactionList = getTransactionList()
    for x in range(0,len(transactionList)):
        transactionValues = web3.eth.getTransaction(transactionList[x])
        if (transactionValues['from'] == from1):
            timeStamp = web3.eth.getBlock(transactionValues.blockNumber).timestamp
            totalTransfers = Transaction(transactionValues['to'],transactionValues['from'],transactionValues['value'],timeStamp)
    return totalTransfers

#Función para retornar el valor total transferido entre un wallet y otro
def getTotalTransfersBetweeenWallets(to,from1):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    transactionList = getTransactionList()
    for x in range(0,len(transactionList)):
        transactionValues = web3.eth.getTransaction(transactionList[x])
        if (transactionValues['to'] == to and transactionValues['from'] == from1):
            timeStamp = web3.eth.getBlock(transactionValues.blockNumber).timestamp
            totalTransfers = Transaction(transactionValues['to'],transactionValues['from'],transactionValues['value'],timeStamp)
        pprint(totalTransfers.date)
    return totalTransfers

#Función para traer una lista con todos los hash de transaccion que se han hecho
def getTransactionList():
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    recentBlock=web3.eth.blockNumber
    Transacciones = []
    HashTransactions = []
    for x in range (1,recentBlock):
        Transacciones.append(web3.eth.getBlock(x).transactions)
    for i in range(0,len(Transacciones)):
        HashTransactions.append(Transacciones[i][0].hex())
    return HashTransactions

#Función para retornar el valor transferido en una transacción
def getTransferedValue(HashTransaccion):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    return web3.eth.getTransaction(HashTransaccion)['value']

#Función para mandar ethereum entre un wallet y otro, retorna el hash de la transaccion
def makeTransaction(de,para,value):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    hashT = binascii.hexlify(web3.eth.sendTransaction({'to':para,'from':de,'value':value}))
    return hashT.decode()

#Función para retornar el balance de una cuenta, recibe como parametro la wallet de la cual se quiere consultar el saldo
def getWalletBalance(Wallet):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    return web3.eth.getBalance(Wallet)

class Transaction:
    def __init__(self,from1,to,value,date):
        self.from1 = from1
        self.to = to
        self.value = value
        self.date = date
 
