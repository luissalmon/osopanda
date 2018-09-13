# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class KYCRequest(models.Model):
    idKYCRequest = models.AutoField(primary_key=True)
    idUser = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class Wallet(models.Model):
    idWallet = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    crationDate = models.DateField()
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
    birdDate = models.DateField()
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