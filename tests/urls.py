from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()



urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

