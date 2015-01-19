from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import Player, PlayerSeasonInfo, Match, PlayerMatchInfo, Goal

admin.site.unregister(Group)
admin.site.unregister(User)


class PlayerAdminForm(forms.ModelForm):
    class Meta:
        labels = {
            'cip': 'CIP'
        }


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerSeasonInfo)
admin.site.register(Match)
admin.site.register(PlayerMatchInfo)
admin.site.register(Goal)
