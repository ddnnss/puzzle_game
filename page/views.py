from django.shortcuts import render
from game.models import Game

def index(request):
    return render(request, 'page/index.html', locals())

def lk(request):
    allGames = Game.objects.filter(player=request.user)
    return render(request, 'page/lk.html', locals())
