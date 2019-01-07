from django.urls import path, include
from . import views
# from . import signals


urlpatterns = [
    path('profile/', views.profile, name="profiles_profile_detail"),
]
