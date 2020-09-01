from django import forms
from .models import BugTicket


class CreateTicket(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ['title', 'description']
        exclude = ['time_filed', 'status']
