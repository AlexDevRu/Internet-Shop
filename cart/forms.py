from django import forms
from .validators import *

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
                                                                'placeholder': 'Enter quantity...',
                                                                'class': 'form-control'
                                                            }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())
