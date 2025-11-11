from django import forms
from .models import Comment, ContactMessage

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
                'pattern': r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$',  # ✅ Requires full domain (.com, .net, etc.)
                'title': 'Please include a full email domain, like example.com or example.net',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Optional phone number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...'
            }),
        }