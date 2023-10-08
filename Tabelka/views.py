from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView
from datetime import datetime

from Tabelka.forms import Tournament5v5Form, Pairings5Form
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
        print("import")
        if form.is_valid():
            result = form.save(commit=False)
            print("commit")
            result.tournament = tournament
            print("t")
            result.save()
            print("t.save")
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
