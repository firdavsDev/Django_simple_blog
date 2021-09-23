from django import forms
from django.db import models
from django.forms import fields

from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = [
            "title",
            'content',
            'activate',
        ]