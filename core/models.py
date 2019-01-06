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


class Profile(models.Model):

    # Fields
    firstName = models.CharField(max_length=244)
    lastName = models.CharField(max_length=244)
    profession = models.CharField(max_length=244)
    birthday = models.DateField()
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.firstName, self.lastName)


class Event(models.Model):

    # Fields
    name = models.CharField(max_length=244)
    slug = models.CharField(max_length=244)
    date = models.DateTimeField()
    text = RichTextUploadingField()
    image = models.ImageField(upload_to="events")

    def get_absolute_url(self):
        return reverse('core_event_detail', args=(self.slug, ))

    def __unicode__(self):
        return u'%s' % self.name


class Service(models.Model):

    # Fields
    name = models.CharField(max_length=244)
    slug = models.CharField(max_length=244)
    icon = models.CharField(max_length=255)
    preText = models.TextField()
    text = RichTextUploadingField()

    def get_absolute_url(self):
        return reverse('core_service_detail', args=(self.slug, ))
    
    def __unicode__(self):
        return u'%s' % self.name

