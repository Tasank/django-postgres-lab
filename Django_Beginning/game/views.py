from django.shortcuts import render
from django.utils.translation import gettext as _ # импортируем функцию для перевода
from django.views import View
from django.http import HttpResponse
from .models import MyModel


class Index(View):
    def get(self, request):
        models = MyModel.objects.all()

        context = {
            'models': models,
        }
        return HttpResponse(render(request, 'index.html', context))
def index(request):
    return render(request, 'index.html')