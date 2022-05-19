from django import forms

from .models import Goal

CHOICES = ((True, 'done'),
           (False, 'not_completed'))

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('title', 'description','priority', 'due_date', 'is_completed')

class GoalFilterForm(forms.ModelForm):
    is_completed = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Goal
        fields = ('is_completed', )
