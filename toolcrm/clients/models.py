from django.db import models
from django.contrib.auth.models import User
        
class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    # auto_now_add -> each time new object created
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add -> each time an object modified
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + self.last_name