from django import forms
from .models import Tournaments5v5

class Tournament5v5Form(forms.ModelForm):
    class Meta:
        model = Tournaments5v5
        fields = '__all__'
        labels = {
            "name": "Nazwa turnieju",
            "player1": "Gracz 1",
            "player2": "Gracz 2",
            "player3": "Gracz 3",
            "player4": "Gracz 4",
            "player5": "Gracz 5",
            "p1": "Armia 1",
            "p2": "Armia 2",
            "p3": "Armia 3",
            "p4": "Armia 4",
            "p5": "Armia 5",
            "date": "Data"
        }