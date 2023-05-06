from rest_framework import serializers

import re

from api.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password", "confirm_password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def validate(self, data):
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
    

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']