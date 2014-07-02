from core.models import Season

def season_list(request):
    return {'season_list': [x.year for x in Season.objects.all()]}
