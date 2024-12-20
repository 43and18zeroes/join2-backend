from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer, RegistrationSerializer, CustomLoginSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data=serializer.errors
            
        return Response(data)
 
class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    print(f"print test")
    
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(f"DEBUG: User - {user}")
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                # 'email': user.email
            }
        else:
            data=serializer.errors
            
        return Response(data)        

class CurrentUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)