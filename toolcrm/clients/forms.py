from django.forms import ModelForm
from .models import Client

class AddClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email', 'description')