from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Team
from .forms import TeamForm

# Create your views here.
@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = TeamForm(data=request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect(to=reverse('myaccount'))
    else:
        form = TeamForm(instance=team)
    return render(request=request, template_name='teams/edit_team.html', context={'team':team, 'form':form})