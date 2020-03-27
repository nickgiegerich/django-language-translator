from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

# Create your views here.

def index(request):
    translator = Translator()
    translations = translator.translate(['Hello world'], dest='ru')

    context = {'translations':translations}
    return render(request, 'dash/main.html', context)