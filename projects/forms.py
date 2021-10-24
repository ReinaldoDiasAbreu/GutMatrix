from django.forms import ModelForm, Textarea, NumberInput
from django.utils.translation import gettext_lazy as _
from .models import Project, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 3}),
        }
        labels = {
            'title': _('Title'),
        }
        help_texts = {
            'title': _('Use puns liberally.'),
        }
        error_messages = {
            'title': {
                'max_length': _("Project name is too long."),
            },
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'gravity', 'urgency', 'trend']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 3, 'required':''}),
            'gravity': NumberInput(attrs={'min': 1, 'max': 5, 'value': '1', 'required':''}),
            'urgency': NumberInput(attrs={'min': 1, 'max': 5, 'value': '1', 'required':''}),
            'trend': NumberInput(attrs={'min': 1, 'max': 5, 'value': '1', 'required':''})
        }
