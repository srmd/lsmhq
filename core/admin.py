from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import Player, Workplace, PlayerSeasonAdmin, Match
from core.models import PlayerAvailability, PlayerMatchStats

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Player)
admin.site.register(Workplace)
admin.site.register(PlayerSeasonAdmin)
admin.site.register(Match)
admin.site.register(PlayerAvailability)
admin.site.register(PlayerMatchStats)
