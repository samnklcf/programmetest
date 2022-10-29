from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('__all__')
        exclude = ('theme','date',)
        

class ConnexionForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisation', max_length=60)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)

class ProfilForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ('__all__')
        # exclude = ('user',)
        