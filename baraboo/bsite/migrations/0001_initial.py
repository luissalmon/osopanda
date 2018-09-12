# Generated by Django 2.1.1 on 2018-09-12 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('idDocument', models.IntegerField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('idDocumentType', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='KYCRequest',
            fields=[
                ('idKYCRequest', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idPerson', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('birdDate', models.DateField()),
                ('lastModification', models.DateTimeField()),
                ('mail', models.EmailField(max_length=254, verbose_name='e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='PersonDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Document')),
                ('idPerson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('idRole', models.IntegerField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=100)),
                ('roleDescription', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('idUser', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Role')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.User')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('idWallet', models.IntegerField(primary_key=True, serialize=False)),
                ('crationDate', models.DateField()),
                ('address', models.CharField(max_length=60)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.User')),
            ],
        ),
        migrations.AddField(
            model_name='kycrequest',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.User'),
        ),
        migrations.AddField(
            model_name='document',
            name='idDocumentType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.DocumentType'),
        ),
    ]
