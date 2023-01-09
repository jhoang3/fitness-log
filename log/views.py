from django.shortcuts import render, redirect
from item.models import Entry
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
# views maybe final layout: index - list of all entries, from latest to first.
# detail - display exercises, reps, and sets of that seeion

# right now, one page displaying
@login_required
def home(request):
    entries = Entry.objects.order_by('-pk')
    context = {'entries': entries}
    return render(request, "log/home.html", context)

def signup(request):
    # if the request data is post, fill it with post data, otherwise blank form
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            new_user = authenticate(username=username,
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, f'Account created for {username}')
            return redirect("/")
    else: 
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {"form": form})

# def user(request):
#     if request.method == "POST":
#         form = EntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     else:
#         form = EntryForm()
#     return render(request, "item/user.html", {"form": form})