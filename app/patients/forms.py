from .models import Analysis
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, Textarea, DateInput


class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['user_name', 'report', 'age', 'date']

        widgets = {
            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            "report": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter report'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publish date'
            }),
        }
