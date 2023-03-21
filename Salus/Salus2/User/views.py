from django.conf import settings
from django.db.models import base
from django.db.utils import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
# from requests import api
from rest_framework.response import Response
from requests.api import head, request

from django.utils.decorators import method_decorator
# from Account.decorator import *
import requests
import random
import json
import inspect
from django.core.mail import message, send_mail, EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponsePermanentRedirect
# from Account.decorator import *

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from .models import *
#import jwt
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework import generics,viewsets, status
from django.contrib import auth
# from .serializers import *
from rest_framework import viewsets, status
from .backends import *
from rest_framework.authtoken.views import ObtainAuthToken
import time
import datetime
from django.db.models import Sum
import re
import jwt
# from django.views.decorators.csrf import csrf_exempt



class SignupApi(APIView):
    def post(self,request):
        data = request.data
        email =data.get('email')
        user_name=data.get('user_name')
        password=data.get('password')
        phone_number=data.get('phone_number')


        if CustomUser.objects.filter(Q(phone_number=phone_number)).exists():
            return Response({'error':{'message':'User have  already registered'}})
        #
        #
        else:
                store_otp = CustomUser.objects.create(phone_number=phone_number)
        #
        #         data_dict = {}
        #         data_dict["OTP"] = otp
        #
                auth_token = jwt.encode(
                                    {'phone_number':phone_number,

                                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                print(auth_token,'this is auth_token')
                authorization = 'Bearer'+' '+str(auth_token)
                #
                response_result = {}
                response = {}
                response_result['result'] = {
                            'result': {'data': 'Register successful',
                            'token':authorization,
                            'user_id':store_otp.id,
                            "phone_number":phone_number,

                            # 'email':user_create.email,
                            # 'role_id': user_role.id,
                            # 'otp':otp
                            # 'result':data_dict

                            }}
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)

        #

class LoginApiView(APIView):
    # breakpoint()
    def post(self,request):
        data = request.data

        phone_number = data.get('phone_number')
        # password=data.get('password')


        # otp = random.randint(100000, 999999)
        response = {}
        if CustomUser.objects.filter(Q(phone_number=phone_number) ).exists():
            print("CustomUser")
            cuser = CustomUser.objects.get(Q(phone_number=phone_number))
            # store_otp = CustomUser.objects.filter(id=cuser.id).update(reset_otp=int(otp))
            data_dict = {}
            # data_dict["OTP"] = otp

            if cuser:

                auth_token = jwt.encode(
                    {'cuser_id':cuser.id,"phone_number":phone_number,
                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+str(auth_token)
                response_result = {}
                response = {}
                response_result['result'] = {
                    'detail': 'Login successfull',


                    'cuser_id':cuser.id,

                    # 'otp':otp,
                    'token':authorization,
                    'status': status.HTTP_200_OK
                    }
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)


            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)

        else:

            response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response(response['error'], status= status.HTTP_401_UNAUTHORIZED)
