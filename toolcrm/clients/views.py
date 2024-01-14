from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import AddClientForm

# Create your views here.
@login_required
def client_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request=request, template_name="clients/clients_list.html", context={'clients':clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return render(request=request, template_name="clients/client_detail.html", context={'client':client})

@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    form = None
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        client = form.save(commit=False)
        client.modified_at = timezone.now()
        client.save()
        messages.success(request=request, message='Client: {} updated successfully.'.format(client.first_name + " " + client.last_name))
        return redirect(to=reverse('client_detail', args=(client.id,)))
    else:
        form = AddClientForm(instance=client)
        return render(request=request, template_name='clients/edit_client.html', context={'form':form})


@login_required
def add_client(request):
    if request.method=="POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            messages.success(request=request, message='Client created successfully.')
            return redirect(reverse('client_list'))
    else:
        form = AddClientForm()
        return render(request=request, template_name="clients/add_client.html", context={'form':form})

@login_required
def client_delete(request, pk):
    lead = get_object_or_404(Client, pk=pk)
    lead.delete()
    messages.success(request=request, message='Client deleted successfully.')
    return redirect(reverse('client_list'))