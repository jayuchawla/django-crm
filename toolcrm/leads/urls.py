from django.urls import path

from .views import add_lead, leads_list, lead_detail, lead_delete, edit_lead
urlpatterns = [
    path(route='', view=leads_list, name='leads_list'),
    path(route='add_lead/', view=add_lead, name='add_lead'),
    path(route='<int:pk>/', view=lead_detail, name='lead_detail'),
    path(route='<int:pk>/delete/', view=lead_delete, name='lead_delete'),
    path(route='<int:pk>/edit/', view=edit_lead, name='edit_lead'),
]