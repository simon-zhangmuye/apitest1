# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/3/28 19:31'

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')



