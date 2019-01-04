from django.contrib import admin
from django import forms
from .models import Article


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
