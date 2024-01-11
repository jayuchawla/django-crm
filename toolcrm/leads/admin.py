from django.contrib import admin
from .models import Lead, Priority, Status

# Register your models here.
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Lead)