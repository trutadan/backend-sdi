from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

import jwt

from api.models.user import User
from api.serializers.user_serializer import UserRegisterSerializer, UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'created_at': ['gte', 'lte']}
    search_fields = ['$first_name', '$last_name', '$username']
    ordering_fields = ['created_at']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAuthenticationView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('Unauthenticated!')

        serializer = UserRegisterSerializer(user)
        
        return Response(serializer.data)


class UserConfirmationView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('Unauthenticated!')

        serializer = UserSerializer(user)
        
        return Response(serializer.data)


def username_exists(request):
    username = request.GET.get('username', '')
    if not username:
        return JsonResponse({'error': 'Username is required.'}, status=400)
    
    user_exists = User.objects.filter(username__iexact=username).exists()
    return JsonResponse({'exists': user_exists})


def email_exists(request):
    email = request.GET.get('email', '')
    if not email:
        return JsonResponse({'error': 'Email is required.'}, status=400)
    
    email_exists = User.objects.filter(email__iexact=email).exists()
    return JsonResponse({'exists': email_exists})