from django import forms

class L1Form(forms.Form):
    fio = forms.CharField(max_length=100)
    age = forms.IntegerField()
    pol = forms.CharField(max_length=100)
    weight = forms.IntegerField()
    height = forms.IntegerField()