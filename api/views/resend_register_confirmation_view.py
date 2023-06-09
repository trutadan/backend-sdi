import pytz
import random
import string
import datetime

from api.models.user import User
from api.views.user_view import ActivateUserAccountView
from api.authentication import CustomUserAuthentication

from config.settings import EMAIL_HOST_USER

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.mail import EmailMessage


class ResendRegisterConfirmationView(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Get current authenticated user
        user_view = ActivateUserAccountView()
        user_data = user_view.get(request).data

        # Check if user's account is already activated
        if user_data.get('is_active'):
            return Response({'message': 'The account is already verified!'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate confirmation code and expiration time
        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        confirmation_expiration = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) + datetime.timedelta(minutes=10)

        # Update user with new confirmation code and expiration time
        user_model = User.objects.get(id=user_data.get('id'))
        user_model.confirmation_code = confirmation_code
        user_model.confirmation_code_expiration = confirmation_expiration
        user_model.save()

        # Send confirmation email with new confirmation code
        subject = 'Confirm your account'
        body = f'Your new confirmation code is {confirmation_code}' # Add body parameter here
        from_email = EMAIL_HOST_USER
        recipient_list = [user_model.email]
        email = EmailMessage(subject, body, from_email, recipient_list)
        email.send()

        return Response({'message': 'Confirmation code resent successfully!'})
