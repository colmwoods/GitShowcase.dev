from django import forms
from .models import Comment, ContactMessage

# Form For Adding/Editing Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'rows': 3,
                'class': 'form-control'
            }),
        }

# Form For Contact Messages


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                # Requires Full Domain (.com, .net, etc.)
                'pattern': r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$',
                'title': (
                    'Please include a full email domain, '
                    'like example.com or example.net'
                ),
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Optional phone number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...'
            }),
        }
