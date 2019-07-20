# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/23 22:42'

import requests
import ast
from django.conf import settings
from SecureHTTP import AESDecrypt


def getKeyPairs():
    response = requests.get('http://127.0.0.1:8881/api/serverKeypair')
    settings.ServerAESkey = '6Q&J-wstnQKhWMDn8f(%rnI%5.8bsRi>'
    data_str = str(response.content, encoding='utf8')
    data_dict = ast.literal_eval(data_str)
    # decrypted = AESDecrypt(settings.ServerAESkey, data_str)
    # data_dict = ast.literal_eval(decrypted)
    settings.ServerPubKey = data_dict['serverPublicKey']
    settings.ServerPrivKey = data_dict['serverPrivateKey']
    settings.ExpiredTime = data_dict['expired']
