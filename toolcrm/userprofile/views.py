from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile

from teams.models import Team

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user = user)
            team = Team.objects.create(name='Team name goes here', created_by=request.user)
            team.members.add(request.user)
            team.save()
            return redirect(to='/login/')
    else:
        form = UserCreationForm()
        return render(request=request, template_name="userprofile/signup.html", context={'form':form})

def login(request):
    if request.method == "POST":
        pass
    else:
        pass

@login_required
def my_account(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request=request, template_name="userprofile/my_account.html", context={'team':team})