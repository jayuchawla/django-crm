from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile = Userprofile.objects.create(user = user)
            return redirect(to='/login/')
    else:
        form = UserCreationForm()
        return render(request=request, template_name="userprofile/signup.html", context={'form':form})

def login(request):
    if request.method == "POST":
        pass
    else:
        pass