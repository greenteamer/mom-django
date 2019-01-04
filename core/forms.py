from django import forms
from .models import Article, Test, TestQuestion, TestQuestionVariant, StudentTest, StudentTestAnswer


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text']
