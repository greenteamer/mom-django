from django.urls import path, include

from . import views




urlpatterns = (
    # urls for Django Rest Framework API
    path('', views.home, name="home"),
    path('articles/', views.articles, name="core_articles_list"),
    path('articles/<slug:slug>/', views.article_detail, name="core_article_detail"),
    path('services/<slug:slug>/', views.service_detail, name="core_service_detail"),
    path('events/', views.events, name="core_events_list"),
    path('events/<slug:slug>/', views.event_detail, name="core_event_detail"),
)
