from django.forms import ModelForm
from .models import Challenge

class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'start_date', 'end_date', 'coordinator', 'description']