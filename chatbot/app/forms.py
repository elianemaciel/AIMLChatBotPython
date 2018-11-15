from django import forms

class ChatbotForm(forms.Form):
    message = forms.CharField(label='Digite a mensagem:', max_length=100)