# Generated by Django 2.1.1 on 2018-09-17 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('active', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('idDocument', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('idDocumentType', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='KYCRequest',
            fields=[
                ('idKYCRequest', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idPerson', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('birthDate', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('lastModification', models.DateTimeField(auto_now=True)),
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
            name='Project',
            fields=[
                ('idProject', models.IntegerField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=150)),
                ('User', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('requiredCapital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('projectPhase', models.CharField(max_length=100)),
                ('projectOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Project')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('idRole', models.AutoField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=100)),
                ('roleDescription', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='StatusRequest',
            fields=[
                ('idStatus', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Role')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransactionLog',
            fields=[
                ('idTransaction', models.AutoField(primary_key=True, serialize=False)),
                ('transactionHash', models.CharField(max_length=80)),
                ('blockHash', models.CharField(max_length=80)),
                ('date', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('idProjectUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.ProjectUser')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('idWallet', models.AutoField(primary_key=True, serialize=False)),
                ('crationDate', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=60)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='kycrequest',
            name='idStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.StatusRequest'),
        ),
        migrations.AddField(
            model_name='kycrequest',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='idDocumentType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.DocumentType'),
        ),
        migrations.AddField(
            model_name='user',
            name='idPerson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsite.Person'),
        ),
    ]
