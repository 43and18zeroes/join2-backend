# from user_auth_app.models import UserProfile
from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type', 'initials']
        extra_kwargs = {
            'email': {'required': False}
        }
        
class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type', 'initials', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    def save(self):
        pw = self.validated_data['password']
        
        account = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            user_color=self.validated_data['user_color'],
            type=self.validated_data['type'],
            initials=self.validated_data['initials']
        )
        account.set_password(pw)
        account.save()
        return account

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'bio', 'location']