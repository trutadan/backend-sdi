from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

import jwt

from api.models.user import User


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('Unauthenticated!')

        return (user, None)