from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django_extensions.db import fields as extension_fields
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):

    # Fields
    name = models.CharField(max_length=244)
    slug = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    text = RichTextUploadingField()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_article_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('core_article_update', args=(self.slug,))
