import json
from itertools import permutations

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
        teamA = [tournament.p1, tournament.p2, tournament.p3, tournament.p4, tournament.p5]
        teamB = [pairing.op1, pairing.op2, pairing.op3, pairing.op4, pairing.op5]
        all_pairings = []
        data_list = []
        for perm in permutations(teamA):
            all_pairings.append(list(zip(perm, teamB)))
        for one_set in all_pairings:
            total = 0
            for i in one_set:
                # i = pairing.p11 ...
                for A in teamA:
                    for B in teamB:
                        if i == (A, B):
                            x = teamA.index(A) + 1
                            y = teamB.index(B) + 1
                            attr = f"p{x}{y}"
                            j = getattr(pairing, attr)
                total += j
            data_list.append([one_set, total])
        green = 0
        yellow = 0
        red = 0
        for i in data_list:
            if i[1] > 1:
                green += 1
            elif i[1] < -1:
                red += 1
            else:
                yellow += 1
        total = green + yellow + red
        green_p = green / total * 100
        yellow_p = yellow / total * 100
        red_p = red / total * 100
        # data = [green_p, yellow_p, red_p]

        ctx = {
            "tournament": tournament,
            "pairing": pairing,
            "tab_pairing_points": tab_pairing_points,
            "tab_col_points": tab_col_points,
            "form": form,
            "green": green,
            "yellow": yellow,
            "red": red,
            "green_p": green_p,
            "yellow_p": yellow_p,
            "red_p": red_p,
            "total": total,
            # "data": json.dumps(data),
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
            # usuwanie sparowanych
            n1 = teamA.index(first_p1) + 1
            n2 = teamA.index(first_p2) + 1
            no1 = teamB.index(first_op1) + 1
            no2 = teamB.index(first_op2) + 1
            teamA2 = teamA.copy()
            teamA2.remove(first_p1)
            teamA2.remove(first_p2)
            teamB2 = teamB.copy()
            teamB2.remove(first_op1)
            teamB2.remove(first_op2)


            all_pairings = []
            data_list = []
            for perm in permutations(teamA2):
                all_pairings.append(list(zip(perm, teamB2)))
            for one_set in all_pairings:
                total = 0
                for i in one_set:
                    # i = pairing.p11 ...
                    for A in teamA2:
                        for B in teamB2:
                            if i == (A, B):
                                x = teamA.index(A) + 1
                                y = teamB.index(B) + 1
                                attr = f"p{x}{y}"
                                j = getattr(pairing, attr)
                    total += j
                data_list.append([one_set, total])
            green = 0
            yellow = 0
            red = 0
            for i in data_list:
                if i[1] > 1:
                    green += 1
                elif i[1] < -1:
                    red += 1
                else:
                    yellow += 1
            total = green + yellow + red
            green_p = green / total * 100
            yellow_p = yellow / total * 100
            red_p = red / total * 100

            ctx = {
                "tournament": tournament,
                "pairing": pairing,
                "first_p1": first_p1,
                "first_op1": first_op1,
                "first_p2": first_p2,
                "first_op2": first_op2,
                "green": green,
                "yellow": yellow,
                "red": red,
                "green_p": green_p,
                "yellow_p": yellow_p,
                "red_p": red_p,
                "total": total,
                "teamA2": teamA2,
                "teamB2": teamB2,
            }
            return render(request, "pairing5v5.html", ctx)


class EditPairing5v5View(View):
    def get(self, request, id, p_id):
        tournament = Tournaments5v5.objects.get(pk=id)
        pairing = Team_of_5.objects.get(pk=p_id)
        form = Pairings5Form(instance=pairing)
        ctx = {
            "tournament": tournament,
            "form": form,
        }
        return render(request, "pairing5v5_edit.html", ctx)

    def post(self, request, id, p_id):
        tournament = Tournaments5v5.objects.get(pk=id)
        pairing = Team_of_5.objects.get(pk=p_id)
        form = Pairings5Form(request.POST, instance=pairing)
        if form.is_valid():
            result = form.save(commit=False)
            result.tournament = tournament
            result.save()
            return redirect("pairing5v5-view", id=id, p_id=p_id)
        else:
            return redirect("index")

class DeletePairing5v5View(View):
    def get(self, request, id, p_id):
        p = Team_of_5.objects.get(pk=p_id)
        p.delete()
        return redirect("tournament-view", id=id)






