from django.shortcuts import render, redirect, get_object_or_404
from item.forms import EntryForm
from .models import Entry
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required()
def user(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            # request.profile.entry.add(form)
            messages.success(request, f'Post created!')
            return redirect("/")
    else:
        form = EntryForm()
    return render(request, "item/user.html", {"form": form})

# take user to detail page
@login_required
def detail(request, id):
    item = get_object_or_404(Entry, pk=id)
    return render(request, "item/detail.html", {"entry": item})

# deletes an entry
@login_required
def delete(request, id):
    item = get_object_or_404(Entry, pk=id)
    item.delete()
    messages.warning(request,f'Post deleted!')
    return redirect("/")