from django import forms
from .models import QuoteRequest


class QuoteRequestForm(forms.ModelForm):

    class Meta:
        model = QuoteRequest

        fields = [
            'name',
            'email',
            'whatsapp',
            'service',
            'project_title',
            'requirements',
            'deadline',
            'word_count',
            'budget',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email address'
            }),

            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'WhatsApp number'
            }),

            'service': forms.Select(attrs={
                'class': 'form-select'
            }),

            'project_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Research Project on AI'
            }),

            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe your project requirements...'
            }),

            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'word_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2500'
            }),

            'budget': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your proposed budget'
            }),
        }