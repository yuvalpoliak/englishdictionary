from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(req):
    return render(req, 'index.html')

def word(req):
    search = req.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    context = {
        'meaning': meaning,
    }
    return render(req, 'word.html', context)