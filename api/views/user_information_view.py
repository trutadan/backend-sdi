from rest_framework import generics, status
from rest_framework.response import Response

from api.authentication import CustomUserAuthentication

from api.serializers.user_information_serializer import UserInformationSerializer

from rest_framework.permissions import IsAuthenticated


class UserInformationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInformationSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
