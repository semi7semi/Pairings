from django import forms
from .models import Tournaments5v5, Team_of_5


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
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "player1": forms.TextInput(attrs={"class":"form-control"}),
            "player2": forms.TextInput(attrs={"class": "form-control"}),
            "player3": forms.TextInput(attrs={"class": "form-control"}),
            "player4": forms.TextInput(attrs={"class": "form-control"}),
            "player5": forms.TextInput(attrs={"class": "form-control"}),
            "p1": forms.Select(attrs={"class": "form-select mb-3"}),
            "p2": forms.Select(attrs={"class": "form-select mb-3"}),
            "p3": forms.Select(attrs={"class": "form-select mb-3"}),
            "p4": forms.Select(attrs={"class": "form-select mb-3"}),
            "p5": forms.Select(attrs={"class": "form-select mb-3"}),
            "date": forms.DateInput(attrs={"class": "form-control"})
        }

class Pairings5Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Pairings5Form, self).__init__(*args, **kwargs)
        for i in ["p11", "p12", "p13", "p14", "p15", "p21", "p22", "p23", "p24", "p25", "p31", "p32", "p33", "p34",
                  "p35", "p41", "p42", "p43", "p44", "p45", "p51", "p52", "p53", "p54", "p55"]:
            self.fields[i].widget.attrs["min"] = -3
            self.fields[i].widget.attrs["max"] = 3
            self.fields[i].initial = 0
    class Meta:
        model: Team_of_5
        fields = '__all__'
        labels = {
            "name": "Przeciw komu?",
            "op1": "Przeciwnik 1",
            "op2": "Przeciwnik 2",
            "op3": "Przeciwnik 3",
            "op4": "Przeciwnik 4",
            "op5": "Przeciwnik 5",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "op1": forms.TextInput(attrs={"class":"form-control"}),
            "op2": forms.TextInput(attrs={"class": "form-control"}),
            "op3": forms.TextInput(attrs={"class": "form-control"}),
            "op4": forms.TextInput(attrs={"class": "form-control"}),
            "op5": forms.TextInput(attrs={"class": "form-control"}),
        }
