import re
from rest_framework import serializers

from api.models.user import User

from api.serializers.user_address_serializer import UserAddressSerializer
from api.serializers.user_profile_serializer import UserProfileSerializer

class UserInformationSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer()
    profile = UserProfileSerializer()

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'date_joined', 'password', 'confirmation_code', 'confirmation_code_expiration', 'groups', 'user_permissions']
    
    def validate(self, data):
        if not data['zip_code'].isdigit():
            raise serializers.ValidationError('Zip code must contain only digits!')
        
        if not data['phone'].isdigit():
            raise serializers.ValidationError('Phone number must contain only digits!')
        
        if len(data['phone']) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits long!')
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            raise serializers.ValidationError("Invalid email address format.")

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        
        if not data['username'].isalnum():
            raise serializers.ValidationError("Username can only contain letters and numbers.")
        
        if len(data['username']) < 4:
            raise serializers.ValidationError("Username must be at least 4 characters long.")
        
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?!.*\s).{8,}$', data['password']):
            raise serializers.ValidationError("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.")
        
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        
        user = self.instance or self.Meta.model(**data)
        if user.username.lower() in data['password'].lower():
            raise serializers.ValidationError("Password is too weak.")
        
        return data