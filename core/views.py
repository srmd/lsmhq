from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from core.models import Match, Player, PlayerSeasonInfo


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'

class CalendarView(generic.TemplateView):
    template_name = 'core/calendar.html'

class StatsView(generic.TemplateView):
    template_name = 'core/stats.html'

class AdminView(generic.TemplateView):
    template_name = 'core/admin.html'

class MatchView(generic.ListView):
    template_name = 'core/matches.html'
    model = Match

class SeasonView(generic.ListView):
    template_name = 'core/season.html'
    model = PlayerSeasonInfo

class PlayersView(generic.ListView):
    template_name = 'core/players.html'
    model = Player

class PlayerCreate(generic.edit.CreateView):
    model = Player
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:players')

class PlayerUpdate(generic.edit.UpdateView):
    model = Player
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:players')

def deletePlayer(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.delete()
    return HttpResponseRedirect(reverse_lazy('core:players'))
