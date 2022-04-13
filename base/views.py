from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Python project'},
    {'id': 2, 'name': 'FrontEnd'},
    {'id': 3, 'name': 'Backend'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': rooms}
    return render(request, 'base/room.html')
