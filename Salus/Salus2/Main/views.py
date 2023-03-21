from django.db.utils import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
import requests
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from .models import *
import jwt
from django.db.models import Q
from rest_framework import viewsets, status
from django.http import *
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib import auth
import random
from Main.decorators import *

from .backends import *
# from django.views.decorators.http import require_GET

# from security_decorators import need_jwt_verification
# from django.views.decorators.csrf import csrf_exempt
# @require_GET
# @need_jwt_verification
# @csrf_exempt

# This class is used to create Form detail.

class CompanyAPIView(APIView):
    # AutorizationRequired(checkAuthData)
    @method_decorator([AutorizationRequired], name='dispatch')
    # @method_decorator([need_jwt_verification], name="dispatch")
    def post(self,request):
        data = request.data
        name = data.get('name')
        # if Authorization:
        if data:
            company=Company.objects.create(name=name)
            auth_token = jwt.encode(
                    {"name":name,
                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
            authorization = 'Bearer'+' '+str(auth_token)
            response_result = {}
            response = {}
            response_result['result'] = {
                'detail': 'data added successfull',


                # 'cuser_id':cuser.id,

                # 'otp':otp,
                'token':authorization,
                'status': status.HTTP_200_OK
                }
            response['Authorization'] = authorization
            response['status'] = status.HTTP_200_OK
            return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)

            return Response({"Message":"Data Sucessfully Added"})
        else:
            return Response({"Error":"Data Already Exists"})


    # @method_decorator([need_jwt_verification], name="dispatch")
    def get(self,request):
        # CheckAuth(request)
        id = request.query_params.get('id')
        if request.user.is_authenticated:
            data=Company.objects.filter(id=id).values()
            if id:
                aa=Company.objects.all().values()
                return Response(aa)
            else:
                return Response('The user is not Authenticated')
                # response_result = {}
                # response={}
                # response_result['Error'] = {
                #     'Code':'AUTHENTICATION_FAILURE',
                #     "message": "You are not authorized to perform this operation."
                #     }
                # return Response(response_result['Error'])
        else:
            response_result = {}
            response_result['Error'] = {
                    'Code':'AUTHENTICATION_FAILURE',
                    "message": "You are not authorized to perform this operation."
                    }
            return Response(response_result['Error'])


    def put(self,request):
        # CheckAuth(request)
        data=request.data
        print(data)
        id = data.get('id')
        if id:
            data =Company.objects.filter(id=id).update(name=data.get('name'))
            if data:
                return Response({"Data":"Data Updated Sucessfully"})
            else:
                return Response({"Error":"Invalid Id"})
        else:
            return Response({"Error":"Id Required"})


    def delete(self,request):
        # CheckAuth(request)
        id =self.request.query_params.get('id')
        if id:
            data =Company.objects.filter(id=id).delete()
            return Response({"Data":"Data Deleted Sucessfully"})
        else:
            return Response({"Error":"Id Required"})


class StudyinformationAPIView(APIView):
    # CheckAuth(request)
    def post(self,request):
        #breakpoint()
        data = request.data
        company_id=data.get('company_id')
        business_unit=data.get('business_unit')
        facility=data.get('facility')
        project_id=data.get('project_id')
        project_name=data.get('project_name')
        start_date=data.get('start_date')
        end_data=data.get('end_date')
        doc_name=data.get('doc_name')
        scope=data.get('scope')
        objective=data.get('objective')
        if data:
            information=Studyinformation.objects.create(
                company_id_id=company_id,
                business_unit=business_unit,
                facility=facility,
                project_id=project_id,
                project_name=project_name,
                start_date=start_date,
                end_date=end_data,
                doc_name=doc_name,
                scope=scope,
                objective=objective
                )
            return Response({"Message":"Data Sucessfully Added"})
        else:
            return Response({"Error":"Data Required"})

    def get(self,request):
        # CheckAuth(request)
        id =request.query_params.get('id')
        if id:
            data=Studyinformation.objects.filter(id=id).values()
            return Response(data)
        else:
            data = Studyinformation.objects.all().values()
            return Response(data)


    def put(self,request):
        # CheckAuth(request)
        data=request.data
        print(data)
        id = data.get('company_id')
        if id:
            data =Studyinformation.objects.filter(id=id).update(company_id=data.get('company_id'),business_unit=data.get('business_unit'),
                    facility=data.get('facility'),project_id=data.get('project_id'),project_name=data.get('project_name'),doc_name=data.get('doc_name'),
                    scope=data.get('scope'),objective=data.get('objective')
                    )
            if data:
                return Response({"Data":"Data Updated Sucessfully"})
            else:
                return Response({"Error":"Invalid Id"})
        else:
            return Response({"Error":"Id Required"})


    def delete(self,request):
        # CheckAuth(request)
        id =self.request.query_params.get('id')
        if id:
            data =Company.objects.filter(id=id).delete()
            return Response({"Data":"Data Deleted Sucessfully"})
        else:
            return Response({"Error":"Id Required"})
