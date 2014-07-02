from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^calendar$', views.CalendarView.as_view(), name='calendar'),
    url(r'^stats$', views.StatsView.as_view(), name='stats'),
    url(r'^admin$', views.AdminView.as_view(), name='admin'),
    url(r'^admin/(?P<year>\d+)/matches$', views.MatchView.as_view(), name='matches'),
    url(r'^admin/match_create$', views.MatchCreate.as_view(), name='match_create'),
    url(r'^admin/match_update/(?P<pk>\d+)$',
        views.MatchUpdate.as_view(), name='match_update'),
    url(r'^admin/match_delete$', views.MatchDelete.as_view(), name='match_delete'),
    url(r'^admin/(?P<year>\d+)/season$', views.SeasonView.as_view(), name='season'),
    url(r'^admin/season_create$', views.SeasonCreate.as_view(), name='season_create'),
    url(r'^admin/season_update/(?P<pk>\d+)$', views.SeasonUpdate.as_view(), name='season_update'),
    url(r'^admin/players$', views.PlayersView.as_view(), name='players'),
    url(r'^admin/player_create$', views.PlayerCreate.as_view(), name='player_create'),
    url(r'^admin/player_update/(?P<pk>\d+)$', views.PlayerUpdate.as_view(), name='player_update'),
    url(r'^admin/player_delete$', views.PlayerDelete.as_view(), name='player_delete'),
)
