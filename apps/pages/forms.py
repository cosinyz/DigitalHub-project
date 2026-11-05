from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@mail.com', 'required': True}),
            'phone': forms.TelInput(attrs={'placeholder': '+7 (___) ___-__-__'}),
            'message': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Расскажите о проекте', 'required': True}
            ),
        }
