from django.http import JsonResponse
from django.shortcuts import render
from .models import Game

LEVELS = {150:1, 120:2, 100:3}

def start(request):
    print('start game')
    print(request.POST)
    try:
        puzzle_length = int(request.POST.get('puzzle_length'))
        level = LEVELS[puzzle_length]
        print(level)
    except:
        return JsonResponse({'code': 400, 'error': 'Invalid puzzle_length'})
    else:
        game = Game()
        print('game',game)
        game.level = level
        if request.user.is_authenticated:
            game.player = request.user
        game.save()
        print('game info', game.id)

        return JsonResponse({'code': 200, 'image': game.image.url, 'game_id': game.id, 'level': level})


def win(request):
    pass