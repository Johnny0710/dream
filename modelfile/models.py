from datetime import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    lock = models.BooleanField(default=True)
    create_time = models.DateTimeField(default=datetime.now())
    last_time = models.DateTimeField(null=True)
    last_ip = models.CharField(max_length=15, null=True)
    login_time = models.DateTimeField(null=True)

class Role(models.Model):
    r_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8)
    nick_name = models.CharField(max_length=12, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    user = models.OneToOneField('User', related_name='role', on_delete=models.CASCADE)

class Hirer(models.Model):
    h_id = models.AutoField(primary_key=True)

    user = models.OneToOneField('User', related_name='hirer', on_delete=models.CASCADE)

class Employer(models.Model):
    e_id = models.AutoField(primary_key=True)

    user = models.OneToOneField('User',related_name='employer', on_delete=models.CASCADE)

