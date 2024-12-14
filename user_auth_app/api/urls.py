# from .views import UserProfileList, UserProfileDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'registration', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-list'),
]