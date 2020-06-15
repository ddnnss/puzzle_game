from django.shortcuts import render
from game.models import Game,Level

def index(request):
    indexPage = True

    return render(request, 'page/index.html', locals())

def game(request):
    level1 = Level.objects.get(id=1)
    level2 = Level.objects.get(id=2)
    level3 = Level.objects.get(id=3)

    return render(request, 'page/game.html', locals())

def lk(request):
    if request.user.is_authenticated:
        allGames = Game.objects.filter(player=request.user).order_by('-date')
        user = request.user
        return render(request, 'page/lk.html', locals())
    else:
        return render(request, 'page/index.html', locals())
