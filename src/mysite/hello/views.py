from django.http import HttpResponse
from django.shortcuts import render
# What the user sees when getting to a particular route

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')
