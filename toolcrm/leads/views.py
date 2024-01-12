from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead

# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)
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
            lead.save()
            return redirect('dashboard')
    else:
        form = AddLeadForm()
        return render(request=request, template_name="leads/add_lead.html", context={'form':form})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead_name = "{} {}".format(lead.first_name, lead.last_name)
    lead.delete()
    return redirect(to='leads_list')
