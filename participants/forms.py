from django import forms

from .models import Participant

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = '__all__'