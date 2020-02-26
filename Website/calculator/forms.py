from django import forms


# The form which the equation will be written on
class TextEquation(forms.Form):
    equation = forms.CharField(label="f(x)", max_length=30, widget=forms.TextInput(attrs={'id' : 'equation'}))
