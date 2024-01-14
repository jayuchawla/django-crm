from django.urls import path

from .views import edit_team

urlpatterns = [
    path(route='<int:pk>/edit/', view=edit_team, name='edit_team')
]