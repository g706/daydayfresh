#coding:utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)  #采用加密40字节
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=20,default='')
    uaddress = models.CharField(max_length=50,default='')
    uyoubian = models.CharField(max_length=10,default='')
    uphone = models.CharField(max_length=11,default='')
    class Meta:
        db_table = 'userinfo'
