from django.shortcuts import render
from .models import Portfolio

def home(request):
	portfolio = Portfolio.objects.all()
	return render(request, 'portfolio/home.html', {'projects' : portfolio})
