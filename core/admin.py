from django.contrib import admin
from django import forms
from .models import Article, Profile, Event, Service


class ArticleAdminForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['created', 'last_updated']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Article, ArticleAdmin)


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['firstName', 'lastName']


admin.site.register(Profile, ProfileAdmin)


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ['name', 'date']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Event, EventAdmin)


class ServiceAdminForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Service, ServiceAdmin)
