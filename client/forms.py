from django import forms
import django
from django.db.models.lookups import PatternLookup
from django.forms import widgets
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm=forms.CharField(max_length=50 ,widget=forms.PasswordInput,label=_('Parollar takrorlang'))


    def clean_confirm(self):
        if self.cleaned_data['confirm']!=self.cleaned_data['password']:
            raise ValidationError(_('Iltimos bir xil parol kiriting !'))
        
        return self.cleaned_data['confirm']
    class Meta:
        model=User
        fields=['username','password']

        labels={
            'username':_('Login'),
            'password':_('Parol')

        }

        help_texts={
            'username':_("Lotin harflari va sonlar bo'lishi lozim")
        }
        widgets={
            'password':forms.PasswordInput
        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,label=_('Login'),required=True)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput,label=_('Parol'),required=True)


