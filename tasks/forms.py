from django.forms import ModelForm
from .models import Guion

class GuionForm(ModelForm):
    class Meta:
        model = Guion
        fields = ['title', 'description', 'important', 'actor_position']
