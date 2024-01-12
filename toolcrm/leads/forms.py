from django.forms import ModelForm
from .models import Lead

class AddLeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'email', 'description', 'priority', 'status')