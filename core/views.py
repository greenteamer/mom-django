from .models import Article
from django.shortcuts import render


def home(request):
    context = {
        "about": Article.objects.filter(slug="about").first(),
    }
    return render(request, 'core/home.html', context)
