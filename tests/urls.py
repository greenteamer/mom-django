from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()



urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    path('tests/', views.tests, name="tests_tests_list"),
    path('tests/<slug:slug>/', views.TestDetail.as_view(), name="tests_test_detail"),
)

