from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView
from datetime import datetime

from Tabelka.forms import Tournament5v5Form, Pairings5Form, FirstPairingForm
from Tabelka.models import Tournaments5v5, Team_of_5

HELLO_TEXT = "Witaj, dziala!"

class Landing_page(View):
    def get(self, request):
        text = HELLO_TEXT
        t5v5_list = Tournaments5v5.objects.all().order_by("-date")
        ctx = {
            "text": text,
            "t5v5_list": t5v5_list,
        }
        return render(request, "index.html", ctx)


class Index(View):
    def get(self, request):
        pass


class AddTournament5v5View(View):
    def get(self, request):
        form = Tournament5v5Form(initial={"date": datetime.now()})
        ctx = {
            "form": form,
        }
        return render(request, "add_tournament5v5.html", ctx)

    def post(self, request):
        form = Tournament5v5Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")


class Tournament5v5View(View):
    def get(selfself, request, id):
        tournament = Tournaments5v5.objects.get(pk=id)
        pairings_list = Team_of_5.objects.filter(tournament=tournament.id)
        form = Pairings5Form()
        ctx = {
            "tournament": tournament,
            "pairings_list": pairings_list,
            "form": form,
        }
        return render(request, "tournament5v5.html", ctx)

    def post(self, request, id):
        tournament = Tournaments5v5.objects.get(pk=id)
        form = Pairings5Form(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.tournament = tournament
            result.save()
            return redirect("tournament-view", id=id)
        else:
            return redirect("index")


class EditTournament5v5View(View):
    def get(self, request, id):
        tournament = Tournaments5v5.objects.get(pk=id)
        form = Tournament5v5Form(instance=tournament)
        ctx = {
            "form": form,
        }
        return render(request, "add_tournament5v5.html", ctx)

    def post(self, request, id):
        tournament = Tournaments5v5.objects.get(pk=id)
        form = Tournament5v5Form(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect("index")

class DeleteTournament5v5View(View):
    def get(self, request, id):
        t = Tournaments5v5.objects.get(pk=id)
        t.delete()
        return redirect("index")

class Pairing5v5View(View):
    def get(self, request, id, p_id):
        tournament = Tournaments5v5.objects.get(pk=id)
        pairing = Team_of_5.objects.get(pk=p_id)
        form = FirstPairingForm()
        p1 = [pairing.p11, pairing.p12, pairing.p13, pairing.p14, pairing.p15]
        p2 = [pairing.p21, pairing.p22, pairing.p23, pairing.p24, pairing.p25]
        p3 = [pairing.p31, pairing.p32, pairing.p33, pairing.p34, pairing.p35]
        p4 = [pairing.p41, pairing.p42, pairing.p43, pairing.p44, pairing.p45]
        p5 = [pairing.p51, pairing.p52, pairing.p53, pairing.p54, pairing.p55]
        sum_p1 = sum(p1)
        sum_p2 = sum(p2)
        sum_p3 = sum(p3)
        sum_p4 = sum(p4)
        sum_p5 = sum(p5)
        col1 = [pairing.p11, pairing.p21, pairing.p31, pairing.p41, pairing.p51]
        col2 = [pairing.p12, pairing.p22, pairing.p32, pairing.p42, pairing.p52]
        col3 = [pairing.p13, pairing.p23, pairing.p33, pairing.p43, pairing.p53]
        col4 = [pairing.p14, pairing.p24, pairing.p34, pairing.p44, pairing.p54]
        col5 = [pairing.p15, pairing.p25, pairing.p35, pairing.p45, pairing.p55]
        sum_col1 = sum(col1)
        sum_col2 = sum(col2)
        sum_col3 = sum(col3)
        sum_col4 = sum(col4)
        sum_col5 = sum(col5)
        tab_pairing_points = [
            [p1, sum_p1],
            [p2, sum_p2],
            [p3, sum_p3],
            [p4, sum_p4],
            [p5, sum_p5],
        ]
        tab_col_points = [sum_col1, sum_col2, sum_col3, sum_col4, sum_col5]


        ctx = {
            "tournament": tournament,
            "pairing": pairing,
            "tab_pairing_points": tab_pairing_points,
            "tab_col_points": tab_col_points,
            "form": form,
        }
        return render(request, "pairing5v5.html", ctx)

    def post(self, request, id, p_id):
        tournament = Tournaments5v5.objects.get(pk=id)
        pairing = Team_of_5.objects.get(pk=p_id)
        teamA = [tournament.p1, tournament.p2, tournament.p3, tournament.p4, tournament.p5]
        teamB = [pairing.op1, pairing.op2, pairing.op3, pairing.op4, pairing.op5]
        form = FirstPairingForm(request.POST)
        if form.is_valid():
            first_p1 = form.cleaned_data["first_p1"]
            first_op1 = form.cleaned_data["first_op1"]
            first_p2 = form.cleaned_data["first_p2"]
            first_op2 = form.cleaned_data["first_op2"]
            print(first_p1)
            # # do usuwania kolumn
            # n1 = teamA.index(first_p1) + 1
            # n2 = teamA.index(first_p2) + 1
            # no1 = teamB.index(first_op1) + 1
            # no2 = teamB.index(first_op2) + 1
            # teamBpost = teamB.copy()
            # teamBpost.remove(first_op1)
            # teamBpost.remove(first_op2)
            # teamApost = teamA.copy()
            # teamApost.remove(first_p1)
            # teamApost.remove(first_p2)
            ctx = {
                "tournament": tournament,
                "pairing": pairing,
            }
            return render(request, "pairing5v5.html", ctx)
