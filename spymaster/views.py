from django.shortcuts import render
from game.models import *

# Create your views here.

def spymaster_page(request):
    game_board = Card.objects.all()
    turn = Board.objects.first()
    blue_team = Team.objects.get(is_blue=True)
    red_team = Team.objects.get(is_blue=False)
    if request.method == 'POST':
        clues = request.POST
        hint = Clue(clue=clues['clue'],num_of_cards=clues['moves'],team = turn.active_team)
        hint.save()
        turn.guesses_allowed = int(clues['moves']) + 1
        turn.save()
    blue_hints = Clue.objects.filter(team=blue_team)
    red_hints = Clue.objects.filter(team=red_team)
    return render(request, 'spymaster_hooks.html',{'game_board':game_board,'turn':turn,'blue_team':blue_team,
                                                   'red_team':red_team,'blue_hints':blue_hints,'red_hints':red_hints})
