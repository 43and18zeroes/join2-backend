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
    phone_number = serializers.CharField(write_only=True, required=False, allow_blank=True)
    user_color = serializers.CharField(write_only=True, required=False)
    type = serializers.ChoiceField(choices=UserProfile.TYPE_CHOICES, write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'user_color', 'type']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
        )
        user.set_password(self.validated_data['password'])
        user.save()

        # Create a UserProfile for the user
        UserProfile.objects.create(
            user=user,
            phone_number=self.validated_data.get('phone_number', ''),
            user_color=self.validated_data.get('user_color', ''),
            type=self.validated_data.get('type', 'user_from_signup')
        )

        return user

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'bio', 'location']