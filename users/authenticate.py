# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/3/28 20:53'

from rest_framework import exceptions
from .models import *
from rest_framework.authentication import BaseAuthentication


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        user_token_obj = Token.objects.filter(token=token).first()
        if user_token_obj: #认证成功
            return user_token_obj.user, token
        else:
            raise exceptions.AuthenticationFailed("验证失败!")

