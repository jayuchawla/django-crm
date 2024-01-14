from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead

from clients.models import Client
from teams.models import Team

# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
    return render(request=request, template_name="leads/leads_list.html", context={'leads':leads})

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    return render(request=request, template_name="leads/lead_detail.html", context={'lead':lead})

@login_required
def add_lead(request):
    if request.method=="POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            # NOTE: the request user may own multiple teams, we select the first one
            lead.team = Team.objects.filter(created_by=request.user)[0]
            lead.save()
            messages.success(request=request, message='Lead created successfully.')
            return redirect(reverse('leads_list'))
    else:
        form = AddLeadForm()
        return render(request=request, template_name="leads/add_lead.html", context={'form':form})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead_name = "{} {}".format(lead.first_name, lead.last_name)
    lead.delete()
    messages.success(request=request, message='Lead: {} deleted successfully.'.format(lead_name))
    return redirect(to='leads_list')

@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    form = None
    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        lead = form.save(commit=False)
        lead.modified_at = timezone.now()
        lead.save()
        messages.success(request=request, message='Lead: {} updated successfully.'.format(lead.first_name + " " + lead.last_name))
        return redirect(to=reverse('lead_detail', args=(lead.id,)))
    else:
        form = AddLeadForm(instance=lead)
        return render(request=request, template_name='leads/edit_lead.html', context={'form':form})
    
@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    client = Client.objects.create(
        first_name = lead.first_name,
        last_name = lead.last_name,
        email = lead.email,
        description = lead.description,
        created_by = request.user,
        team = Team.objects.filter(created_by=request.user)[0]
    )
    lead.converted_to_client = True
    lead.save()
    messages.success(request=request, message='Lead: {} coverted to client.'.format(lead.first_name + " " + lead.last_name))
    return redirect(reverse('leads_list'))