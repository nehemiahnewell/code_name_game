from django.forms import ModelForm
from game.models import Card

# Create your models here.

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['selected']
