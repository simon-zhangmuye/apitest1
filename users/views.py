from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
import hashlib, time
from django.conf import settings
from django.core.cache import cache
# Create your views here.


def get_random_str(user):
    ctime = str(time.time())
    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(ctime, encoding="utf8"))
    return md5.hexdigest()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # name = request._request._body.get("data").get("username")
        # pwd = request._request._body.get("data").get("password")
        name = request.data.get("username")
        pwd = request.data.get("password")
        user = User.objects.filter(username=name, password=pwd).first()
        res = {"state_code": 200}
        if user:
            random_str = get_random_str(user.username)
            cache.set(random_str, {"username": user.username, "usertype": user.user_type}, timeout=60*60)
            res['msg'] = "success"
            res["token"] = random_str
        else:
            res["state_code"] = 401
            res["msg"] = "用户名或密码错误"
        return JsonResponse(res)


# class UserView(APIView):
#     def post(self, request, *args, **kwargs):
#         token = request.data.get("token")
#         print(token)
#         user = cache.get(token)
#         res = {"state_code": 200}
#         if user:
#             res['msg'] = "success"
#             res['username'] = user.username
#             res['user_type'] = user.user_type
#         else:
#             res["state_code"] = 405
#             res["msg"] = "no such a user"
#         return JsonResponse(res)


class ServerPublicKey(APIView):
    def get(self, request):
        res = {"state_code": 200}
        res['serverPublicKey'] = settings.ServerPubKey
        res['expired'] = settings.ExpiredTime

        return JsonResponse(res)


