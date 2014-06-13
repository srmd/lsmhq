import datetime
from decimal import Decimal

from django.db import models


def current_year():
    return datetime.date.today().year


def make_choices(choices, *extra):
    return [(choice, choice) for choice in choices] + list(extra)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,
                           choices=(('M', 'Male'), ('F', 'Female')))
    year_joined = models.PositiveIntegerField(default=current_year)

    date_of_birth = models.DateField(blank=True, null=True)
    workplace = models.ForeignKey('Workplace', blank=True, null=True)
    cip = models.CharField(max_length=6, blank=True, null=True)
    work_number = models.CharField(max_length=50, blank=True, null=True)
    home_number = models.CharField(max_length=50, blank=True, null=True)
    cell_number = models.CharField(max_length=50, blank=True, null=True)
    work_email = models.EmailField(blank=True, null=True)
    home_email = models.EmailField(blank=True, null=True)

    @property
    def full_name(self):
        return ' '.join((self.first_name, self.last_name))

    def __unicode__(self):
        return self.full_name


class Workplace(models.Model):
    address = models.CharField(max_length=200)

    def __unicode__(self):
        return self.address


class PlayerSeasonAdmin(models.Model):
    player = models.ForeignKey(Player)
    year = models.PositiveIntegerField(default=current_year)
    type = models.CharField(max_length=1,
                            choices=(('R', 'Regular'), ('S', 'Substitute')))
    owed = models.DecimalField(max_digits=5, decimal_places=2,
                               default=Decimal('0.00'))
    paid = models.DecimalField(max_digits=5, decimal_places=2,
                               default=Decimal('0.00'))
    payment_type = models.CharField(max_length=2,
                                    choices=(('CA', 'Cash'), ('CH', 'Cheque')))

    def __unicode__(self):
        return '%s (%d)' % (self.player.full_name, self.year)

    class Meta:
        verbose_name_plural = "player season admin"


class Match(models.Model):
    date = models.DateField()

    def __unicode__(self):
        return self.date.strftime('%B %d %Y')

    class Meta:
        verbose_name_plural = "matches"


class PlayerAvailability(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    rating = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s rated %d on %s: %s' % (self.player.full_name, self.rating,
                                          self.match, self.available)

    class Meta:
        verbose_name_plural = "player availabilities"


class PlayerMatchStats(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    team = models.CharField(max_length=1, choices=make_choices('12'))
    position = models.CharField(max_length=1, choices=make_choices('AMDG'))
    goals = models.PositiveIntegerField(default=0)
    shootout_goals = models.PositiveIntegerField(default=0)
    penalty_goals = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    stars = models.CharField(max_length=1, null=True, default=None,
                             choices=[(None, 'N/A')] + make_choices('123'))

    def __unicode__(self):
        return '%s (%s)' % (self.player.full_name, self.match)

    class Meta:
        verbose_name_plural = "player match stats"
