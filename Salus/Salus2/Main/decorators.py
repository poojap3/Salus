from rest_framework.response import Response
import jwt
from rest_framework import authentication, exceptions,status
from django.conf import settings
from django.contrib.auth.models import User
from django.http.response import JsonResponse

def AutorizationRequired(func):
    def checkAuthData(request,*args, **kwargs):

        try:
            if ('Authorization' in request.headers) and (len(request.headers['Authorization']) != 0):
                pass
            else:

                return JsonResponse({'error': {'code': 'AUTHENTICATION_FAILURE', 'message': 'You are not authorized to perform this operation. '}}, status=status.HTTP_401_UNAUTHORIZED)

            auth_data = request.headers['Authorization']
            if not auth_data:
                return JsonResponse(
                    {'error': {'code': 'NO_HEADER_FOUND', 'message': 'pass an Auth header '}}, status=status.HTTP_401_UNAUTHORIZED)
            if "Bearer " not in auth_data:
                return JsonResponse(
                    {'error': {'code': 'NO_TOKEN_FOUND', 'message': 'pass token '}}, status=status.HTTP_401_UNAUTHORIZED)
            auth_data = auth_data.split(' ')[1]

        except IndexError as e:
            return Response({'error': {'message': e}})

        try:
            print(settings.JWT_SECRET_KEY, '==========secret-key===========')
            payload = jwt.decode(auth_data, str(
                settings.JWT_SECRET_KEY), algorithms="HS256")

            print(payload,'playloaded')
            if payload['user_name']:
                print('this is payload')
                role_name = payload['user_name']
                if role_name == 'ADMIN':
                    print('admin')

                    return 1
                elif role_name == 'USER':
                    print('User')
                    return 2

                else:
                    return 3
            else:
                return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'this token is not valid'}}, status=status.HTTP_401_UNAUTHORIZED)


        except jwt.DecodeError as identifier:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You token is not valid'}}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.ExpiredSignatureError as identifier:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'token expired!,enter valid token'}}, status=status.HTTP_401_UNAUTHORIZED)
        return func(request,*args, **kwargs)
    return checkAuthData
