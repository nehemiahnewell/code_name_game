from django.views.generic import ListView, UpdateView
from django.shortcuts import render
from game.models import *

# Create your views here.


def spy_page(request):
    game_board = Card.objects.all()
    turn = Board.objects.first()
    blue_team = Team.objects.get(is_blue=True)
    red_team = Team.objects.get(is_blue=False)
    moved = {'moved': False}
    if request.method == 'POST':
        moved = {'moved': True}
        flip = request.POST['value']
        if flip != 'end':
            card_to_flip = Card.objects.get(word = flip)
            card_to_flip.selected = True
            card_to_flip.save(update_fields=['selected'])
            # if it's a blue card
            if card_to_flip.card_type == card_to_flip.BLUE:
                agent = Team.objects.get(is_blue = True)
                agent.spies_left = agent.spies_left -1
                #blue has one less card to find.
                agent.save()
                #save this now
                if agent.spies_left == 0:
                    return render(request, 'victory.html',{'blue_team':blue_team, 'red_team':red_team,})
                elif turn.is_blue == True:
                    turn.guesses_allowed = turn.guesses_allowed -1
                else:
                    turn.guesses_allowed = 0
            #if it's a red cardd
            if card_to_flip.card_type == card_to_flip.RED:
                agent = Team.objects.get(is_blue = False)
                agent.spies_left = agent.spies_left -1
                #red has one less card to find
                agent.save()
                #save it now
                if agent.spies_left == 0:
                    return render(request, 'victory.html',{'blue_team':blue_team, 'red_team':red_team,})
                elif turn.is_blue == False:
                    turn.guesses_allowed = turn.guesses_allowed -1
                else:
                    turn.guesses_allowed = 0
            # if it's a bystandard, end the turn
            if card_to_flip.card_type == card_to_flip.BEIGE:
                turn.guesses_allowed = 0
            #if it's an assassin, end he game
            if card_to_flip.card_type == card_to_flip.BLACK:
                return render(request, 'assassin.html',{'turn':turn})
        else:
            turn.guesses_allowed = 0
        if turn.guesses_allowed == 0:
            turn.is_blue = not turn.is_blue
            turn.active_team = Team.objects.get(is_blue=turn.is_blue)
        turn.save()


    blue_hints = Clue.objects.filter(team=blue_team)
    red_hints = Clue.objects.filter(team=red_team)
    return render(request, 'spy.html',{'game_board':game_board,'turn':turn,'blue_team':blue_team,
                                                   'red_team':red_team,'blue_hints':blue_hints,'red_hints':red_hints, 'moved':moved})
