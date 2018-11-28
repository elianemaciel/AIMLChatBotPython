from django import forms

class ChatbotForm(forms.Form):
    message = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite a mensagem'}))
