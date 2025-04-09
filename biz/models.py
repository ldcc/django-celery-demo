from django.db import models
from django_cryptography.fields import encrypt


# 城市
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


# 数据中心
class IDC(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


# 主机
class Host(models.Model):
    name = models.CharField(max_length=100)
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    root_password = models.CharField(max_length=128)  # todo 加密
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 密码修改记录
class PasswordHistory(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)
    changed_at = models.DateTimeField(auto_now_add=True)


# 主机统计
class HostStatistic(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(auto_now_add=True)


# 耗时统计
class RequestLog(models.Model):
    path = models.CharField(max_length=255)
    duration = models.FloatField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
