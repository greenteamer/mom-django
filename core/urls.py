from django.urls import path, include
from rest_framework import routers

from . import api
from tests import api as tests_api
from profiles import api as profiles_api
from . import views

router = routers.DefaultRouter()
router.register(r'article', api.ArticleViewSet)
router.register(r'test', tests_api.TestViewSet)
router.register(r'testquestion', tests_api.TestQuestionViewSet)
router.register(r'testquestionvariant', tests_api.TestQuestionVariantViewSet)
router.register(r'studenttest', tests_api.StudentTestViewSet)
router.register(r'studenttestanswer', tests_api.StudentTestAnswerViewSet)
router.register(r'user', profiles_api.UserViewSet, basename="user")


urlpatterns = (
    # urls for Django Rest Framework API
    path('', views.home, name="home"),
    path('articles/', views.articles, name="core_articles_list"),
    path('articles/<slug:slug>/', views.article_detail, name="core_article_detail"),
    path('services/<slug:slug>/', views.service_detail, name="core_service_detail"),
    path('events/', views.events, name="core_events_list"),
    path('events/<slug:slug>/', views.event_detail, name="core_event_detail"),
    path('api/v1/', include(router.urls)),
)
