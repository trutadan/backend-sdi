from rest_framework import serializers

from api.models.user_profile import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['phone'].isdigit():
            raise serializers.ValidationError('Phone number must contain only digits!')
        
        if len(data['phone']) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits long!')
        
        return data
    
    class Meta:
        model = UserProfile
        fields = "__all__"