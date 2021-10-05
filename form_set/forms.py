from django.forms import (formset_factory, modelformset_factory)
from .models import *
from django import forms




class invoiceForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name here'
                }
            )
        }

orderFormset = modelformset_factory(Lineitem, fields=('product','rate','quantity',),
widgets={
            'product':forms.Select(attrs={'class':'form-control'}),
            'rate':forms.TextInput(attrs={'class':'form-control',}),
            'quantity':forms.TextInput(attrs={'class':'form-control',}),
}
)
