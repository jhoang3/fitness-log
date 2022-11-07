from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry
from datetime import datetime

# Create your views here.
# views starting layout: index - list of all entries, from latest to first.
# detail - display exercises, reps, and sets of that seeion
def home(request):
    return render(request, "log/home.html",
                    {'current_time': datetime.now(),
                    "entries": Entry.objects.all(),
                    "num_entries": Entry.objects.count(),})

def detail(request):
    return render(request, "log/detail.html")