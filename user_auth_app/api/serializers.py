from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth import authenticate
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
            username=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.set_password(self.validated_data['password'])
        user.save()

        UserProfile.objects.create(
            user=user,
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data.get('phone_number', ''),
            user_color=self.validated_data.get('user_color', ''),
            type=self.validated_data.get('type', 'user_from_signup')
        )

        return user
    

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('email')
        password = data.get('password')
        
        # Sonderprüfung für gast@gast.de und 123456
        if username == 'guest@example.com' and password == '123456':
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': 'Guest',
                    'last_name': 'User',
                }
            )
            if created:
                user.set_password(password)
                user.save()

                # UserProfile anlegen
                UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': 'Guest',
                        'last_name': 'User',
                        'type': 'user_from_signup',
                        'user_color': '#66EB90',
                    }
                )

            # Authentifizierung fortsetzen
            user = authenticate(username=username, password=password)

        # Normale Authentifizierung
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Ungültige E-Mail oder Passwort.")
        
        data['user'] = user
        return data


class ContactCreationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True, required=False, allow_blank=True)
    user_color = serializers.CharField(write_only=True, required=False)
    type = serializers.ChoiceField(choices=UserProfile.TYPE_CHOICES, write_only=True, required=False)

    class Meta:
        model = UserProfile  # oder User, falls User primär ist
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type']

    def save(self):
        user = User.objects.create(
            username=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )

        user_profile = UserProfile.objects.create(
            user=user,
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data.get('phone_number', ''),
            user_color=self.validated_data.get('user_color', ''),
            type=self.validated_data.get('type', 'user_from_contactbook')
        )

        return user_profile  # Das Objekt zurückgeben, damit die ID enthalten ist

    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type', 'initials']
#         extra_kwargs = {
#             'email': {'required': False}
#         }