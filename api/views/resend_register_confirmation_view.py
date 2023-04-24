from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from django.core.mail import send_mail

import random
import string
import datetime

from api.models.user import User


class ResendRegisterConfirmationView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_confirmed:
            return Response({'message': 'Account is already confirmed'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a new confirmation code and expiration time
        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        confirmation_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)

        # Save the new confirmation code and expiration time to the user
        user.confirmation_code = confirmation_code
        user.confirmation_code_expiration = confirmation_expiration
        user.save()

        # Send the new confirmation email
        subject = 'Confirm your account'
        message = f'Your new confirmation code is {confirmation_code}'
        from_email = 'noreply@example.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return Response({'message': 'New confirmation email sent'})