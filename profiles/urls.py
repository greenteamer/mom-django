from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.profile, name="profiles_profile_detail"),
]
