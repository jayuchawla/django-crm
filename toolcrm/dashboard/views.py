from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from leads.models import Lead
from clients.models import Client
from teams.models import Team

# Create your views here.
@login_required
def dashboard(request):
    # NOTE: the request user may own multiple teams, we select the first one
    user_team = Team.objects.filter(created_by=request.user)[0]
    top_leads = Lead.objects.filter(team=user_team, converted_to_client=False).order_by('-created_at')[:5]
    print(top_leads)
    top_clients = Client.objects.filter(team=user_team).order_by('-created_at')[:5]
    return render(request=request, template_name='dashboard/dashboard.html', context={'leads':top_leads, 'clients':top_clients})