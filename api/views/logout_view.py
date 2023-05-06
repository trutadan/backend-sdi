from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from api.authentication import CustomUserAuthentication


class LogoutView(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt', path="/")
        response.data = {
            'message': 'success'
        }
        return response
