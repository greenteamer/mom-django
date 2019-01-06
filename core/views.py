from .models import Article, Event, Service
from django.shortcuts import render


def home(request):
    context = {
        "about": Article.objects.filter(slug="about").first(),
        "forAll": Article.objects.filter(slug="for-all").first(),
        "events": Event.objects.all(),
        "services": Service.objects.all(),
    }
    return render(request, 'core/home.html', context)


def articles(request):
    context = {
        "title": "Статьи",
        "items": Article.objects.all(),
    }
    return render(request, 'core/common/list.html', context)


def article_detail(request, slug):
    context = {
        "item": Article.objects.filter(slug=slug).first(),
    }
    return render(request, 'core/common/detail.html', context)


def service_detail(request, slug):
    context = {
        "item": Service.objects.filter(slug=slug).first(),
    }
    return render(request, 'core/common/detail.html', context)



def events(request):
    context = {
        "title": "События",
        "items": Event.objects.all(),
    }
    return render(request, 'core/common/list.html', context)


def event_detail(request, slug):
    context = {
        "item": Event.objects.filter(slug=slug).first(),
    }
    return render(request, 'core/common/detail.html', context)
