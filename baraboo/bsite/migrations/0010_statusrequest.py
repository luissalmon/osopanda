# Generated by Django 2.1.1 on 2018-09-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsite', '0009_user_idperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusRequest',
            fields=[
                ('idStatus', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
