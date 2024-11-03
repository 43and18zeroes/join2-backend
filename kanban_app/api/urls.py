from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubtaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path, include
# from .views import TaskViewSet
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]