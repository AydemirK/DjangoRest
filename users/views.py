from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from users.models import ActivationCode
from .serializers import UserCreateSerializer, UserLoginSerializer, UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        
        user = User.objects.create_user(username=username, password=password, is_active=False)
        
        code = ''.join(random.choices('0123456789', k=6))
        # print(code)
        ActivationCode.objects.create(user=user, code=code)
        
        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)



# @api_view(['POST'])
# def registration_api_view(request):
    
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
    
#     user = User.objects.create_user(username=username, password=password, is_active=False)
    
#     code = ''.join(random.choices('0123456789', k=6))
#     print(code)
#     ActivationCode.objects.create(user=user, code=code)
    
    
#     return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED) 

class ConfirmUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data.get('user_id')
        code = serializer.validated_data.get('code')

        try:
            activation_code = ActivationCode.objects.get(user_id=user_id, code=code)
            user = activation_code.user
            user.is_active = True
            user.save()
            activation_code.delete()
            return Response(data={'status': 'User activated'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(data={'status': 'Invalid code or user'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def confirm_user_api_view(request):
#     serializer = UserConfirmSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     user_id = serializer.validated_data.get('user_id')
#     code = serializer.validated_data.get('code')
#     print(code)

#     try:
#         activation_code = ActivationCode.objects.get(user_id=user_id, code=code)
#         user = activation_code.user
#         user.is_active = True
#         user.save()
#         activation_code.delete()
#         return Response(data={'status': 'User activated'}, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist:
#         return Response(data={'status': 'Invalid code or user'}, status=status.HTTP_400_BAD_REQUEST)

class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'User credentials are wrong!'})

# @api_view(['POST'])
# def authorization_api_view(request):
    
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
    
#     user = authenticate(username=username, password=password)
    
#     if user:
        
#         token, _ = Token.objects.get_or_create(user=user)   
         
#         return Response(data={'key': token.key})
    
#     return Response(status=status.HTTP_401_UNAUTHORIZED, data={'User credent are wrong!'})