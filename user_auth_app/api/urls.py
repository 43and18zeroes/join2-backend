from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('profiles/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('current-user/', views.CurrentUserProfileView.as_view(), name='current-user'),
    path('create-contact/', views.UserViewSet.as_view({'post': 'create'}), name='create-contact')
]