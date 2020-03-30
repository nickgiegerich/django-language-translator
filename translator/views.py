from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

from .models import *

# Create your views here.

def index(request):

    alphabet = Alphabet.objects.all()
    numbers = Number.objects.all()

    
    translator = Translator()
    translations = translator.translate([''], dest='ru')

    context = {'translations':translations, 'alphabet':alphabet, 'numbers':numbers}
    return render(request, 'dash/index.html', context)

def alphabetModal(request, pk): 

    letter = Alphabet.objects.get(id=pk)

    print('getting called')

    context = {'letter':letter}

    return render(request, 'dash/alphaModal.html', context)