from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Passenger, Train, Security, Staff
import datetime
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')
