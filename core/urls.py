from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^calendar$', views.CalendarView.as_view(), name='calendar'),
    url(r'^stats$', views.StatsView.as_view(), name='stats'),
    url(r'^admin$', views.AdminView.as_view(), name='admin'),
    url(r'^admin/players$', views.PlayersView.as_view(), name='players'),
    url(r'^admin/player_create$', views.PlayerCreate.as_view(), name='player_create'),
)
