# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models

# Create your models here.

class KYCRequest(models.Model):
    idKYCRequest = models.AutoField(primary_key=True)
    idUser = models.ForeignKey('User', on_delete=models.CASCADE)
    reference = models.CharField(max_length=1000)
    idStatus = models.ForeignKey('StatusRequest', on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    def create_user(self, userName, password, Person, code):
        """
        Creates and saves a User with the given username and password.
        """

        user = self.model(
            username=userName
        )
        user.set_password(password)
        user.idPerson = Person
        user.confirmationCode = code
        user.save()
        return user

    def create_superuser(self):
        return None
    
class User(AbstractBaseUser):
    #idUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    idPerson = models.ForeignKey('Person', on_delete=models.CASCADE)
    active = models.IntegerField(default=1)
    confirm = models.BooleanField(default=False)
    confirmationCode = models.CharField(max_length=32, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

class Wallet(models.Model):
    idWallet = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    crationDate = models.DateField(auto_now=True)
    address = models.CharField(max_length=60)

class UserRole(models.Model):
    idUser = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    idRole = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
    )

class Role(models.Model):
    idRole = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=100)
    roleDescription = models.CharField(max_length=150)

class Person(models.Model):
    idPerson = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    birthDate = models.DateField()
    country = models.CharField(max_length=50)
    lastModification = models.DateTimeField(auto_now=True)
    mail = models.EmailField('e-mail', blank=False)

class DocumentType(models.Model):
    idDocumentType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

class Document(models.Model):
    idDocument = models.AutoField(primary_key=True)
    path = models.CharField(max_length=250)
    idDocumentType = models.ForeignKey(
        'DocumentType',
        on_delete=models.CASCADE,
    )

class PersonDocument(models.Model):
    idPerson = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )
    idDocument = models.ForeignKey(
        'Document',
        on_delete=models.CASCADE,
    )

class StatusRequest(models.Model):
    idStatus = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

class Project(models.Model):
    idProject = models.IntegerField(primary_key=True)
    projectName = models.CharField(max_length=150)
    User = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    requiredCapital = models.DecimalField(max_digits=10, decimal_places=2)
    projectPhase = models.CharField(max_length=100)
    projectOwner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

class ProjectUser(models.Model):
    idProject = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
    )
    idUser = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )

class UserTransactionLog(models.Model):
    idTransaction = models.AutoField(primary_key=True)
    transactionHash = models.CharField(max_length=80)
    blockHash = models.CharField(max_length=80)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    transactionStatus = models.BooleanField(default=False)
    idProjectUser = models.ForeignKey(
        'ProjectUser',
        on_delete=models.CASCADE
)

class PresentationProjectData(models.Model):
    idpresentationProjectData = models.AutoField(primary_key=True)
    idProject = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    returnOfInversion = models.DecimalField(max_digits=3, decimal_places=2)
    expirationDate = models.DateField()
    initialInvestmentRound = models.DecimalField(max_digits=10, decimal_places=2)
    taretCapital = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.FileField(upload_to='videos/%m/%d')

class ImageType(models.Model):
    idImageType = models.AutoField(primary_key=True)
    imageType = models.CharField(max_length=100)


class PresentationProjectImage(models.Model):
    idPresentationProjectImage = models.AutoField(primary_key=True)
    idPresentationProjectData = models.ForeignKey(
        'PresentationProjectData',
        on_delete=models.CASCADE,
    )
    idImageType = models.ForeignKey(
        'ImageType',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='images/%m/%d')