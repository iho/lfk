from django import forms
from django.forms import ModelForm

from core.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        exclude = 'user'



