from django.http import request
from django.shortcuts import render
from . models import User, Message

# Create your views here.
def user ():
      pass
def message ():
    pass
def index (request):
    return render (request, 'bages/index.html')
