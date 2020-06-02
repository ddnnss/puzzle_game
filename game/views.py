import json

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
        if request.user.is_authenticated:
            game = Game(player=request.user, game_type=int(request.POST.get('game_type')))
        else:
            game = Game(game_type=int(request.POST.get('game_type')))
        print('game',game)
        game.level = level
        game.save()
        print('game info', game.id)

        return JsonResponse({'code': 200, 'image': game.image.url, 'game_id': game.id, 'level': level})

def win(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    game = Game.objects.get(id=request_body['game_id'])
    game.result = True
    game.save()
    game.player.rating += game.get_win_rating()
    game.player.save()
    return JsonResponse({'rating': game.player.rating})