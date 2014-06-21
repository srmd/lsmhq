from django.views import generic

from core.models import Player


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'

class PlayersView(generic.ListView):
    template_name = 'core/players.html'
    model = Player
