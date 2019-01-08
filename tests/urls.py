from django.urls import path, include

from . import views


urlpatterns = (
    # urls for Django Rest Framework API
    path('tests/', views.tests, name="tests_tests_list"),
    path('tests/<str:id>/', views.TestDetail.as_view(), name="tests_test_detail"),
)

