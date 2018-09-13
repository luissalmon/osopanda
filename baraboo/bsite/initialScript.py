from bsite.models import DocumentType, Role, Person, User, UserRole, Wallet, KYCRequest, Document, PersonDocument

doct = DocumentType(name="INE", description="Identificacion oficial")
doct.save()

rol = Role(roleName="Inversionista", roleDescription="ejemplo")
rol.save()

per = Person(name="BDJGL", lastName="baraboo", birdDate="2018-02-05", mail="tata@tata.com")
per.save()

ptemp = Person.objects.get(idPerson=1)
u = User(userName="usuario", password="contraseña", idPerson=ptemp, active=1)
u.save()

utemp = User.objects.get(idUser=1)
roltemp = Role.objects.get(idRole=1)
ur = UserRole(idUser=utemp, idRole=roltemp)
ur.save()

wal = Wallet(idUser=utemp, address="")
wal.save()

kyc = KYCRequest(idUser=utemp)
kyc.save()

dttemp = DocumentType.objects.get(idDocumentType=1)
doc = Document(path="/Users/luis/Desktop/respaldo beto/Music/iTunes/iTunes Media/Music/Electric Guest/Mondo",
    idDocumentType=dttemp)
doc.save()

idctemp = Document.objects.get(idDocument=1)
pd = PersonDocument(idPerson=ptemp, idDocument=idctemp)
pd.save()