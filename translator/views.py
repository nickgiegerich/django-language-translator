from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

# Create your views here.

def index(request):

    russAlph = {
        'Аа':'a',
        'Бб':'b',
        'Вв':'v',
        'Гг':'g',
        'Дд':'d',
        'Ее':'e, ye',
        'Ёё':'yo, jo, ë',
        'Жж':'zh, ž',
        'Зз':'z',
        'Ии':'i',
        'Йй':'y, i, j',
        'Кк':'k',
        'Лл':'l',
        'Мм':'m',
        'Нн':'n',
        'Оо':'o',
        'Пп':'p',
        'Рр':'r',
        'Сс':'s',
        'Тт':'t',
        'Уу':'u',
        'Фф':'f',
        'Хх':'kh, h, x',
        'Цц':'ts, c',
        'Чч':'ch, č',
        'Шш':'sh, š',
        'Щщ':'shch, sch, šč',
        'Ъъ':'ʺ',
        'Ыы':'y',
        'Ьь':'"',
        'Ээ':'e, è',
        'Юю':'yu, ju',
        'Яя':'ya, ja',
    }

    
    translator = Translator()
    translations = translator.translate([''], dest='ru')

    context = {'translations':translations, 'alphabet':russAlph}
    return render(request, 'dash/main.html', context)