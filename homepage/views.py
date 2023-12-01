from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def run_homepage(request):
    # return HttpResponse("hlelo")
    return render(request, 'index.html')