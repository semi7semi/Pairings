"""Semi_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Tabelka.views import Landing_page, AddTournament5v5View, EditTournament5v5View, DeleteTournament5v5View, \
     Tournament5v5View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Landing_page.as_view(), name="index"),
    path('t5v5/add/', AddTournament5v5View.as_view(), name="add-5v5"),
    path('t5v5/<int:id>/', Tournament5v5View.as_view(), name="tournament-view"),
    path('t5v5/edit/<int:id>/', EditTournament5v5View.as_view(), name="edit-5v5"),
    path('t5v5/delete/<int:id>/', DeleteTournament5v5View.as_view(), name="delete-5v5"),


]
