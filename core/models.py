import datetime
from decimal import Decimal

from django.db import models


def current_year():
    return datetime.date.today().year


def choices(choices, *extra):
    return [(choice, str(choice)) for choice in choices] + list(extra)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,
                           choices=(('M', 'Male'), ('F', 'Female')))

    date_of_birth = models.DateField(blank=True, null=True)
    workplace = models.CharField(max_length=200, blank=True, null=True)
    cip = models.CharField(max_length=6, blank=True, null=True)
    work_number = models.CharField('number (work)',
                                   max_length=50, blank=True, null=True)
    home_number = models.CharField('number (home)',
                                   max_length=50, blank=True, null=True)
    cell_number = models.CharField('number (cell)',
                                   max_length=50, blank=True, null=True)
    work_email = models.EmailField('email (work)',
                                   blank=True, null=True)
    home_email = models.EmailField('email (home)',
                                   blank=True, null=True)

    @property
    def full_name(self):
        return ' '.join((self.first_name, self.last_name))

    def __unicode__(self):
        return self.full_name


class Season(models.Model):
    year = models.PositiveIntegerField(default=current_year)
    regular_rate = models.DecimalField(max_digits=5, decimal_places=2,
                               default=Decimal('0.00'))
    substitute_rate = models.DecimalField(max_digits=5, decimal_places=2,
                           default=Decimal('0.00'))

    def __unicode__(self):
        return 'Season %d' % self.year


class PlayerSeasonInfo(models.Model):
    player = models.ForeignKey(Player)
    season = models.ForeignKey(Season)
    type = models.CharField(max_length=1,
                            choices=(('R', 'Regular'), ('S', 'Substitute')))
    owed = models.DecimalField(max_digits=5, decimal_places=2,
                               default=Decimal('0.00'))
    paid = models.DecimalField(max_digits=5, decimal_places=2,
                               default=Decimal('0.00'))
    payment_type = models.CharField(max_length=2,
                                    choices=(('CA', 'Cash'), ('CH', 'Cheque')))

    @property
    def balance(self):
        return self.owed - self.paid

    def __unicode__(self):
        return '%s (%d)' % (self.player.full_name, self.year)


class Match(models.Model):
    date = models.DateField()
    season = models.ForeignKey(Season)
    cancelled = models.BooleanField(default=False)

    def status(self):
        if self.cancelled:
            return 'Cancelled'
        if datetime.date.today() < self.date:
            return 'Pending'
        return 'Played'

    def get_score(self):
        all_goals = Goal.objects.filter(match=self)
        goals_by_team = [PlayerMatchInfo.objects.filter(player=goal.player,
                         match=goal.match).team for goal in all_goals]
        return '%d - %d' % (goals_by_team.count('1'), goals_by_team.count('2'))

    def __unicode__(self):
        return '%s: %s' % (self.date.strftime('%B %d %Y'), self.status())

    class Meta:
        verbose_name_plural = "matches"


class PlayerMatchInfo(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    rating = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    position_A = models.PositiveIntegerField(choices=choices((1, 2, 3, 4)))
    position_M = models.PositiveIntegerField(choices=choices((1, 2, 3, 4)))
    position_D = models.PositiveIntegerField(choices=choices((1, 2, 3, 4)))
    position_G = models.PositiveIntegerField(choices=choices((1, 2, 3, 4)))

    team = models.CharField(max_length=1, null=True, default=None,
                            choices=[(None, 'N/A')] + choices('12'))
    position = models.CharField(max_length=1, choices=choices('AMDG'))

    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    star = models.CharField(max_length=1, null=True, default=None,
                            choices=[(None, 'N/A')] + choices('123'))

    def __unicode__(self):
        return '%s (%s)' % (self.player.full_name, self.match)


class Goal(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    minute = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=1,
                            choices=(('R', 'Regular'), ('P', 'Penalty'),
                                     ('O', 'Own'), ('S', 'Shootout')))

    def __unicode__(self):
        return '%s (%s)' % (self.player.full_name, self.match)
