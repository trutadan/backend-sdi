import pytz
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import EmailMessage

import random
import string
import datetime

from api.serializers.user_serializer import UserRegisterSerializer
from config.settings import EMAIL_HOST_USER

from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate confirmation code and expiration time
        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        confirmation_expiration = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) + datetime.timedelta(minutes=10)
        
        # Save confirmation code and expiration time to user
        user.confirmation_code = confirmation_code
        user.confirmation_code_expiration = confirmation_expiration
        user.save()

        # Send confirmation email
        subject = 'Confirm your account'
        message = f'Your confirmation code is {confirmation_code}'
        from_email = EMAIL_HOST_USER
        recipient_list = [user.email]
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

        return Response({'message': 'Account created successfully!'})
