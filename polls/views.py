from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):
    return HttpResponse("hello")
