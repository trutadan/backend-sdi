from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

import datetime

from api.models.user import User


class ConfirmRegisterView(APIView):
    def get(self, request, confirmation_code):
        user = User.objects.filter(confirmation_code=confirmation_code).first()

        if user is None:
            return Response({'message': 'Invalid confirmation code!'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if confirmation code has expired
        if datetime.datetime.utcnow() > user.confirmation_code_expiration:
            return Response({'message': 'Confirmation code has expired!'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.confirmation_code = None
        user.confirmation_code_expiration = None
        user.save()

        return Response({'message': 'Account activated successfully!'})
