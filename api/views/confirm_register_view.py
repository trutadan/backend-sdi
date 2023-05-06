import datetime
import pytz

from api.models.user import User
from api.views.user_view import ActivateUserAccountView
from api.authentication import CustomUserAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ConfirmRegisterView(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, confirmation_code):
        # Get current authenticated user
        user_view = ActivateUserAccountView()
        user_data = user_view.get(request).data

        # Check if user's account is already activated
        if user_data.get('is_active'):
            return Response({'message': 'The account is already verified!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user has provided a confirmation code
        if not confirmation_code:
            return Response({'message': 'Please provide a confirmation code!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user's confirmation code matches the provided code
        if user_data.get('confirmation_code') != confirmation_code:
            return Response({'message': 'Invalid confirmation code!'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if confirmation code has expired
        if datetime.datetime.now(tz=pytz.UTC) > datetime.datetime.fromisoformat(user_data.get('confirmation_code_expiration')):
            return Response({'message': 'Confirmation code has expired!'}, status=status.HTTP_400_BAD_REQUEST)

        # Activate user's account
        user_model = User.objects.get(id=user_data.get('id'))
        user_model.is_active = True
        user_model.confirmation_code = None
        user_model.confirmation_code_expiration = None
        user_model.save()

        return Response({'message': 'Account activated successfully!'})
