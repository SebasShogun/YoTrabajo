from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
def about(request):
    return render(request, "about/about.html")