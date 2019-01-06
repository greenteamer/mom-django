from django.shortcuts import render
from tests.models import Test
from django.views.generic.base import TemplateView


# Create your views here.
def tests(request):
    context = {
        "title": "Тесты",
        "items": Test.objects.all(),
    }
    return render(request, 'core/common/list.html', context)


class TestDetail(TemplateView):
    template_name = 'tests/detail.html'

    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = Test.objects.filter(slug=slug).first()
        return context

    def post(self, request, slug):
        print(u'>>>> %s', request.method)
    


# def test_detail(request, slug):
#     context = {
#         "test": Test.objects.filter(slug=slug).first(),
#     }
#     return render(request, 'tests/detail.html', context)