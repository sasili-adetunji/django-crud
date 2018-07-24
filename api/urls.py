from django.conf.urls import url, include
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from .views import (
    UserProfileViewSet,
)


router = DefaultRouter()

router.register('list', UserProfileViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
