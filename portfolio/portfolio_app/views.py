from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import ProjectDetails
# Create your views here.

class HomePage(generic.ListView):
    queryset=ProjectDetails.objects.all()
