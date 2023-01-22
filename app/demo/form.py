from django import forms

class searchForm(forms.Form):
  keyword = forms.CharField(required=False, widget=forms.TextInput(attrs={
    'class': 'search form-control',
    'placeholder': 'tell us about you interested in !'
  }))