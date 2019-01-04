from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'article', api.ArticleViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', views.home, name="home"),
    path('api/v1/', include(router.urls)),
)
