from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import Player, Workplace, PlayerSeasonAdmin, Match
from core.models import PlayerAvailability, PlayerMatchStats

admin.site.unregister(Group)
admin.site.unregister(User)

class PlayerAdminForm(forms.ModelForm):
    class Meta:
        model = Player
        labels = {
            'cip': 'CIP'
        }

class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm


admin.site.register(Player, PlayerAdmin)
admin.site.register(Workplace)
admin.site.register(PlayerSeasonAdmin)
admin.site.register(Match)
admin.site.register(PlayerAvailability)
admin.site.register(PlayerMatchStats)
