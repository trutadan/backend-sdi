import jwt
from rest_framework import generics, status
from rest_framework.response import Response

from api.models.user import User

from api.serializers.user_information_serializer import UserInformationSerializer


class UserInformationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInformationSerializer

    def get_object(self):
        token = self.request.COOKIES.get('jwt')
        
        if not token:
            return None

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload['id']
            return User.objects.get(id=user_id)
        except (jwt.ExpiredSignatureError, User.DoesNotExist):
            return None

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)