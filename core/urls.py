from django.urls import path, include
from rest_framework import routers

from . import api
from tests import api as tests_api
from . import views

router = routers.DefaultRouter()
router.register(r'article', api.ArticleViewSet)
router.register(r'test', tests_api.TestViewSet)
router.register(r'testquestion', tests_api.TestQuestionViewSet)
router.register(r'testquestionvariant', tests_api.TestQuestionVariantViewSet)
router.register(r'studenttest', tests_api.StudentTestViewSet)
router.register(r'studenttestanswer', tests_api.StudentTestAnswerViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', views.home, name="home"),
    path('api/v1/', include(router.urls)),
)
