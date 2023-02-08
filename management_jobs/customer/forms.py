from django import forms

from .models import Customer, Job


class FormCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
