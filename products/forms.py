from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.forms import Form
from .models import Product


#ModelForm bu
class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"sizning title"}))

    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'placeholder':"Your description",
        'class':'new-class-name two',
        'rows':20,
        'cols':120
    })) #widgets orqali biz qulay holga keltirib olishimiz mumkin
    price = forms.DecimalField(initial=199.99)


    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price',
        ]
    
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if "yangi" not in title:
            raise forms.ValidationError('Bu yangi suzi bulishi kk') #forms.ValidationError('xavar') bu xatoliklarni ushlab qolis uchunn
        return title


#Bu django Form
class RawProductForm(forms.Form):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"sizning title"}))

    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'placeholder':"Your description",
        'class':'new-class-name two',
        'rows':20,
        'cols':120
    }))
    price = forms.DecimalField(initial=199.99)