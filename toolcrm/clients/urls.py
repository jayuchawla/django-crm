from django.urls import path

from .views import client_list, client_detail, add_client, edit_client, client_delete

urlpatterns = [
    path(route='', view=client_list, name='client_list'),
    path(route='add_client/', view=add_client, name='add_client'),
    path(route='<int:pk>/', view=client_detail, name='client_detail'),
    path(route='<int:pk>/delete/', view=client_delete, name='client_delete'),
    path(route='<int:pk>/edit/', view=edit_client, name='edit_client'),
]