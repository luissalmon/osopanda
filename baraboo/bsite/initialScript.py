from bsite.models import DocumentType, Role, Person

doc = DocumentType(name="INE", description="Identificacion oficial")
doc.save()

rol = Role(roleName="Inversionista", roleDescription="ejemplo")
rol.save()

per = Person(
    name="",
    lastName="",
    birdDate="",
    lastModification="",
    mail=""
)
per.save()