from django.shortcuts import render
from random import  getrandbits, shuffle
from game.models import *
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def clear_game():
    """Resets all data in the database to nothing"""
    Board.objects.all().delete()
    Card.objects.all().delete()
    Clue.objects.all().delete()
    Team.objects.all().delete()

def create_game_deck():
    """Creates the game"""
    # init deck
    deck = []

    #get starting team
    blueness = bool(getrandbits(1))
    if blueness == 1:
        BLUE = ['bl'] * 9
        RED = ['rd'] * 8
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
        team = Team(is_blue=True,spies_left = 9,)
        team.save()
        team = Team(is_blue=False,spies_left = 8)
        team.save()
        #Sets the team that DOESN'T start, turn switching logic is allowed to switch it to the initial player.
    else:
        BLUE = ['bl'] * 8
        RED = ['rd'] * 9
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
        team = Team(is_blue=True,spies_left = 8)
        team.save()
        team = Team(is_blue=False,spies_left = 9)
        team.save()
    shuffle(deck)
    these_words = []
    for phrase in Dictionary_Words.objects.all():
        these_words.append(phrase.list_of_words)
    shuffle(these_words)
    for card in deck:
        person = Card(word=these_words.pop(),card_type=card)
        person.save()

def set_starting_board_conditions():
    team_to_start = Team.objects.get(spies_left=9)
    starting_line = Board(is_blue = False, guesses_allowed = 0, active_team=team_to_start)
    starting_line.save()

def start_game():
    clear_game()
    create_game_deck()
    set_starting_board_conditions()

def does_game_exist():
    if Card.objects.count() > 0:
        return True
    else:
        return False

def start_index_page(request):

    if request.method == 'POST':
        path = request.POST['start']
        if path == 'start':
            start_game()
        if path == 'reset':
            clear_game()
    if does_game_exist():
        game_exist = {'game': 'started'}
    else:
        game_exist = {'game': 'waiting'}
    return render(request, 'index.html', game_exist)

def select_player(request):
    return render(request, 'select_player.html')


