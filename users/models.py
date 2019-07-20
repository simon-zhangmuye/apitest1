from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """用户表"""
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    user_type = models.IntegerField(choices=((101, "管理员"), (102, "员工"), (201, "普通用户"), (202, "VIP用户")), default=201)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


