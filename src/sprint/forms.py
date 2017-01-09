from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Sprint

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = {'begin', 'end'}
        widgets = {
            'begin': forms.SelectDateWidget(attrs={
                    'class': 'form-control'
                }),
            'end': forms.SelectDateWidget(attrs={
                    'class': 'form-control'
                }
            )
        }