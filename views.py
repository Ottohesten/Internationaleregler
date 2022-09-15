from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import Player
from .forms import RacismPointForm
from .models import RacismPoint

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)

# Create your views here.


def home(request):
    return render(request, "internationaleregler/home.html")


def drengene(request):
    return render(request, "internationaleregler/drengene.html")


class RacismPointCreateView(LoginRequiredMixin, CreateView):
    model = RacismPoint
    fields = ["title", "user", "description", "points"]
    template_name = "internationaleregler/racismelisten_form.html"
    success_url = reverse_lazy("racismelisten")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RacismPointListView(LoginRequiredMixin, ListView):
    model = RacismPoint
    template_name = "internationaleregler/racismelisten.html"
    context_object_name = "rps"
    ordering = ["-date_posted"]
    paginate_by = 20


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        users = User.objects.all()

        for user in users:
            points = 0
            rps = RacismPoint.objects.filter(user=user)
            for rp in rps:
                points += rp.points
            user.player.points = points
            user.player.save()

        players = Player.objects.all().order_by("-points")

        context["users"] = players


        return context


