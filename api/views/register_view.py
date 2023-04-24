from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail

import random
import string
import datetime

from api.serializers.user_serializer import UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate confirmation code and expiration time
        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        confirmation_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        
        # Save confirmation code and expiration time to user
        user.confirmation_code = confirmation_code
        user.confirmation_code_expiration = confirmation_expiration
        user.save()

        # Send confirmation email
        subject = 'Confirm your account'
        message = f'Your confirmation code is {confirmation_code}'
        from_email = 'noreply@example.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return Response(serializer.data)
