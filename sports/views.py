from django.shortcuts import render
from .models import Team, Player, Match
import requests

def home(request):
    teams = Team.objects.all()
    return render(request, 'sports/home.html', {'teams': teams})

def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'sports/team_detail.html', {'team': team, 'players': players})

def match_results(request):
    matches = Match.objects.all()
    return render(request, 'sports/match_results.html', {'matches': matches})

def news(request):
    api_key = 'b3029d33f524b959bde11e9641f2656'
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'category': 'sports',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    print(response.json())  # Add this line to debug
    if response.status_code == 200:
        news_data = response.json()
        return render(request, 'sports/news.html', {'articles': news_data['articles']})
    else:
        return render(request, 'sports/news.html', {'error': 'Failed to retrieve news'})

