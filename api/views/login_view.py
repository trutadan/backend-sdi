from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

import jwt
import datetime

from api.models.user import User

from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        username_or_email = request.data['user']
        password = request.data['password']

        if '@' in username_or_email:
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'expiration': (datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).isoformat(),
            'iat': int(datetime.datetime.utcnow().timestamp())
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True, path="/")
        response.data = {
            'jwt': token
        }

        return response
    