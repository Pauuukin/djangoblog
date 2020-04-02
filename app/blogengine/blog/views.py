from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def posts_list(request):
    names = ['Oleg', 'Masha', 'Vanya', 'Nastya']
    return render(request, 'blog/index.html', context={'names': names})