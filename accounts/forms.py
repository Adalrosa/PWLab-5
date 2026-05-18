from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistoForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório para o Link Mágico.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)