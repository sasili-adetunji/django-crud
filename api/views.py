from rest_framework.viewsets import ModelViewSet, ViewSet
from django.contrib.auth import get_user_model

from rest_framework import filters
from .serializers import (
    UserSerializer,
)
User = get_user_model()



class UserProfileViewSet(ModelViewSet):
    """
    Handles creating reading and updating of user profiles
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)