from django import forms

from .models import Priority, Status, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password',
                  'permissions', 'url', 'description', 'active']
        widgets = {'password': forms.PasswordInput()}


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name']