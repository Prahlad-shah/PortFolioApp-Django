from django import forms
from . import models

class RegisterUser(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = '__all__'