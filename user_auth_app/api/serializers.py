# from user_auth_app.models import UserProfile
from rest_framework import serializers
from user_auth_app.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type', 'initials']
        extra_kwargs = {
            'email': {'required': False}
        }

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'bio', 'location']