from django.shortcuts import render
from tests.models import Test
from django.views.generic.base import TemplateView


# Create your views here.
def tests(request):
    context = {
        # "title": "Тесты",
        # "items": Test.objects.all(),
    }
    return render(request, 'tests/list.html', context)


class TestDetail(TemplateView):
    template_name = 'tests/list.html'

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = Test.objects.filter(id=id).first()
        return context

    def post(self, request, id):
        print(u'>>>> %s', request.method)
