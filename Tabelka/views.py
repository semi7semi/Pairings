from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView
from datetime import datetime


HELLO_TEXT = "Witaj, dziala!"

class Landing_page(View):
    def get(self, request):
        text = HELLO_TEXT
        ctx = {
            "text": text,
        }
        return render(request, "dashboard.html", ctx)

class Index(View):
    def get(self, request):
        pass




