from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Miktar')
    product_id = forms.IntegerField(widget=forms.HiddenInput())
