from rest_framework.viewsets import ModelViewSet, ViewSet
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions, status

from rest_framework import filters
from .serializers import (
    UserSerializer,
)

UserProfile = get_user_model()


class UserProfileViewSet(ModelViewSet):
    """
    Handles creating reading and updating of user profiles
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
