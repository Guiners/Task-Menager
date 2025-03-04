from django import forms
# from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add in a new task"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add in a new description"}))

    class Meta:
        model = Task
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required")
        return title
