from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home(request):
    return HttpResponse(time.strftime("%H:%M"))