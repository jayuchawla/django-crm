from django.db import models
from django.contrib.auth.models import User

from teams.models import Team

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Lead(models.Model):
    
    PRIORITY_CHOICES = [
        (priority.name, priority.name) for priority in Priority.objects.all()
    ]

    STATUS_CHOICES = [
        (status.name, status.name) for status in Status.objects.all()
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_by = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE)
    converted_to_client = models.BooleanField(default=False)
    # auto_now_add -> each time new object created
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add -> each time an object modified
    modified_at = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name + self.last_name