# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/19 5:42'

from django.utils.deprecation import MiddlewareMixin
from SecureHTTP import AESEncrypt, AESDecrypt
from SecureHTTP import RSADecrypt
from django.conf import settings
from django.http import JsonResponse
import ast
from rest_framework.response import Response
from rest_framework import status


class Crypt(MiddlewareMixin):

    def process_request(self, request):
        # if request.path != '/api/serverPublicKey':
            if request.method == 'POST':
                #获取header里边加密的aes key
                encrypted_aeskey = request.META.get('HTTP_KEY')
                #解密aes key
                client_aeskey = RSADecrypt(settings.ServerPrivKey, encrypted_aeskey)
                if client_aeskey == 'ERROR':
                    res = {"status":"5001","msg":"公钥过期，请从新尝试"}
                    return JsonResponse(res)
                #把request.body里边的数据从bytes转成字符串
                data_str = str(request.body, encoding='utf8')
                #字符串变字典
                data_dict = ast.literal_eval(data_str)
                #取data的值解密
                data_dict['data'] = ast.literal_eval(AESDecrypt(client_aeskey, data_dict['data']))
                #解密后的数据转化回bytes赋值request.decryped_data
                request._body = data_dict
                request.aeskey = client_aeskey

    def process_response(self, request, response):
        if request.path != '/api/key':
            data_str = str(response.content, encoding='utf8')
            response.content = AESEncrypt(request.aeskey, data_str)
        return response



