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
        players_points = []
        army_points = []
        for w in range(1, 6):
            p1points = []
            attr2 = f'player{w}'
            attr3 = f'p{w}'
            for z in range(1, 6):
                attr1 = f'p{w}{z}'
                j1 = getattr(pairing, attr1)
                p1points.append(j1)
            av1 = sum(p1points)
            p1points.append(av1)
            player_name = getattr(tournament, attr2)
            player_army = getattr(tournament, attr3)
            player_data = player_name, player_army
            player_p = player_data, p1points
            players_points.append(player_p)
        for w in range(1, 6):
            p2points = []
            for z in range(1, 6):
                attr2 = f'p{z}{w}'
                j2 = getattr(pairing, attr2)
                p2points.append(j2)
            total2 = sum(p2points)
            army_points.append(total2)
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
            "players_points": players_points,
            "army_points": army_points,
            "teamB": teamB,
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
            players_points = []
            army_points = []
            for w in range(1, 6):
                p1points = []
                if w == n1 or w == n2:
                    pass
                else:
                    attr2 = f'player{w}'
                    attr3 = f'p{w}'
                    for z in range(1, 6):
                        if z == no1 or z == no2:
                            pass
                        else:
                            attr1 = f'p{w}{z}'
                            j1 = getattr(pairing, attr1)
                            p1points.append(j1)
                    av1 = sum(p1points)
                    p1points.append(av1)
                    player_name = getattr(tournament, attr2)
                    player_army = getattr(tournament, attr3)
                    player_data = player_name, player_army
                    player_p = player_data, p1points
                    players_points.append(player_p)
            for w in range(1, 6):
                p2points = []
                if w == no1 or w == no2:
                    pass
                else:
                    for z in range(1, 6):
                        if z == n1 or z == n2:
                            pass
                        else:
                            attr2 = f'p{z}{w}'
                            j2 = getattr(pairing, attr2)
                            p2points.append(j2)
                    total2 = sum(p2points)
                    army_points.append(total2)
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
                "players_points": players_points,
                "army_points": army_points,
                "green": green,
                "yellow": yellow,
                "red": red,
                "green_p": green_p,
                "yellow_p": yellow_p,
                "red_p": red_p,
                "total": total,
                "teamB": teamB2,
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






