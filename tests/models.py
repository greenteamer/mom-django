from django.urls import reverse
from django.conf import settings
from django.db import models as models
from django_extensions.db import fields as extension_fields
from ckeditor_uploader.fields import RichTextUploadingField


class Test(models.Model):

    # Fields
    name = models.CharField(max_length=244)
    slug = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    text = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('tests_test_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('tests_test_update', args=(self.slug,))

    def get_questions(self):
        return TestQuestion.objects.filter(test=self)


class TestQuestion(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    text = models.TextField()
    points = models.PositiveIntegerField(default=0)
    answer = RichTextUploadingField(null=True, blank=True)

    # Relationship Fields
    test = models.ForeignKey(
        'tests.Test',
        on_delete=models.CASCADE, related_name="testQuestions"
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s - %s' % (self.test.name, self.name)

    def get_absolute_url(self):
        return reverse('tests_testquestion_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('tests_testquestion_update', args=(self.pk,))


class TestQuestionVariant(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)

    # Relationship Fields
    question = models.ForeignKey(
        'tests.TestQuestion',
        on_delete=models.CASCADE, related_name="testQuestionVariants"
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('tests_testquestionvariant_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('tests_testquestionvariant_update', args=(self.pk,))
