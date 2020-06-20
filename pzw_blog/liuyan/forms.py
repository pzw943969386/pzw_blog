from django import forms
from liuyan.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)