from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _

from .views import (
  UserCreateAPIView,
  UserLoginAPIView
)


urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]