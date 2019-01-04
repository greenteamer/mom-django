from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'test', api.TestViewSet)
router.register(r'testquestion', api.TestQuestionViewSet)
router.register(r'testquestionvariant', api.TestQuestionVariantViewSet)
router.register(r'studenttest', api.StudentTestViewSet)
router.register(r'studenttestanswer', api.StudentTestAnswerViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

