from api.authentication import CustomUserAuthentication
from api.models.user import User
from api.permissions import IsAdmin, IsUserOwner
from api.serializers.user_serializer import UserRegisterSerializer, UserRolesSerializer, UserSerializer

from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdmin,)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'created_at': ['gte', 'lte']}
    search_fields = ['$first_name', '$last_name', '$username']
    ordering_fields = ['created_at']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (CustomUserAuthentication, )
    permission_classes = (IsAuthenticated, (IsUserOwner|IsAdmin),)


class AuthenticatedUserInformationView(APIView):
    serializer_class = UserRegisterSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class ActivateUserAccountView(APIView):
    serializer_class = UserSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])
def username_exists(request):
    username = request.GET.get('username', '')
    if not username:
        return JsonResponse({'error': 'Username is required.'}, status=400)
    
    user_exists = User.objects.filter(username__iexact=username).exists()
    return JsonResponse({'exists': user_exists})


@api_view(['GET'])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])
def email_exists(request):
    email = request.GET.get('email', '')
    if not email:
        return JsonResponse({'error': 'Email is required.'}, status=400)
    
    email_exists = User.objects.filter(email__iexact=email).exists()
    return JsonResponse({'exists': email_exists})


class UserRolesListView(APIView):
    serializer_class = UserRolesSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdmin,)

    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


class UserRolesDetailsView(APIView):
    serializer_class = UserRolesSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdmin,)

    def get_user(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound(detail="User not found!")

    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)