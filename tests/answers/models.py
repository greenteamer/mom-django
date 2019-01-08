from django.urls import reverse
from django.conf import settings
from django.db import models as models
from django_extensions.db import fields as extension_fields
from ckeditor_uploader.fields import RichTextUploadingField

from tests.models import Test, TestQuestion, TestQuestionVariant


class StudentTest(models.Model):

    # Fields
    totalPoints = models.PositiveIntegerField(blank=True, null=True)
    inProgress = models.BooleanField(default=True)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="tests"
    )
    test = models.ForeignKey(
        # 'tests.Test',
        Test,
        on_delete=models.CASCADE, related_name="studentsTests"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('tests_studenttest_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('tests_studenttest_update', args=(self.pk,))


class StudentTestAnswer(models.Model):

    answer = RichTextUploadingField(null=True, blank=True)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="userAnswers"
    )
    studentTest = models.ForeignKey(
        'tests.StudentTest',
        on_delete=models.CASCADE,
        related_name="studentTestAnswers",
    )
    question = models.ForeignKey(
        # 'tests.TestQuestion',
        TestQuestion,
        on_delete=models.CASCADE,
        related_name="questionAnswers",
        null=True,
        blank=True,
    )
    variant = models.ForeignKey(
        # 'tests.TestQuestionVariant',
        TestQuestionVariant,
        on_delete=models.CASCADE,
        related_name="variantAnswers",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('tests_studenttestanswer_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('tests_studenttestanswer_update', args=(self.pk,))

