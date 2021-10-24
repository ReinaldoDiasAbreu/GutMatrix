from django.contrib import admin
from .models import Project
from .models import Task

# Register your models here.

# Adicionando percistência dos models para ser gerenciada no admin
admin.site.register(Project)
admin.site.register(Task)