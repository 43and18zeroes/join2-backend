from rest_framework import generics
# from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer

from rest_framework import viewsets
# from .serializers import UserSerializer
from user_auth_app.models import UserProfile

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer