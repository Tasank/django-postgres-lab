from django.shortcuts import render
from django.utils.translation import gettext as _ # импортируем функцию для перевода
from django.views import View
from django.http import HttpResponse


class Index(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)

def index(request):
    return render(request, 'index.html')