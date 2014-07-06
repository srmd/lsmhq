from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from core.models import Match, Player, PlayerSeasonInfo, Season

class ObjectFromPostMixin(object):
    def get_object(self):
        return get_object_or_404(self.model, pk=self.request.POST['id'])

class IndexView(generic.TemplateView):
    template_name = 'core/index.html'

class CalendarView(generic.TemplateView):
    template_name = 'core/calendar.html'

class StatsView(generic.TemplateView):
    template_name = 'core/stats.html'

class AdminView(generic.TemplateView):
    template_name = 'core/admin.html'

class MatchView(generic.TemplateView):
    template_name = 'core/matches.html'

    def get_context_data(self, **kwargs):
        context = super(MatchView, self).get_context_data(**kwargs)
        context['season'] = Season.objects.get(year=self.kwargs['year'])
        context['season_matches'] = Match.objects.filter(season__year=self.kwargs['year'])
        return context

class MatchCreate(generic.edit.CreateView):
    model = Match
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:matches')

class MatchUpdate(generic.edit.UpdateView):
    model = Match
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:matches')

class MatchDelete(generic.edit.DeleteView):
    success_url = reverse_lazy('core:matches')

    def get_object(self):
        match_id = self.request.POST['match_id']
        return get_object_or_404(Match, pk=match_id)

class SeasonView(generic.TemplateView):
    template_name = 'core/season.html'

    def get_context_data(self, **kwargs):
        context = super(SeasonView, self).get_context_data(**kwargs)
        context['players'] = Player.objects.exclude(playerseasoninfo__season__year__exact=self.kwargs['year'])
        context['season'] = Season.objects.get(year=self.kwargs['year'])
        context['season_players'] = PlayerSeasonInfo.objects.filter(season__year__exact=self.kwargs['year'])
        return context

class SeasonCreate(generic.edit.CreateView):
    model = Season
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse_lazy('core:season', kwargs={'year':self.object.year})

class SeasonUpdate(generic.edit.UpdateView):
    model = Season
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse_lazy('core:season', kwargs={'year':self.object.year})

    def get_object(self):
        return get_object_or_404(Season, year=self.kwargs['year'])

class SeasonDelete(ObjectFromPostMixin, generic.edit.DeleteView):
    model = Season
    success_url = reverse_lazy('core:admin')

def SeasonPlayersCreate(request, pk):
    PlayerSeasonInfo.objects.bulk_create([
        PlayerSeasonInfo(player_id=key, season_id=pk, type=val)
        for key, val in request.POST.items()
        if key != 'csrfmiddlewaretoken' and val
    ])
    return HttpResponseRedirect(reverse_lazy('core:season', kwargs={'year':Season.objects.get(pk=pk).year}))

class SeasonPlayerUpdate(generic.edit.UpdateView):
    model = PlayerSeasonInfo
    template_name = 'core/season_player_update.html'

    def get_success_url(self):
        return reverse_lazy('core:season', kwargs={'year':self.object.season.year})

class SeasonPlayerDelete(ObjectFromPostMixin, generic.edit.DeleteView):
    model = PlayerSeasonInfo

    def get_success_url(self):
        return reverse_lazy('core:season', kwargs={'year':self.object.season.year})

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

class PlayerDelete(ObjectFromPostMixin, generic.edit.DeleteView):
    model = Player
    success_url = reverse_lazy('core:players')
