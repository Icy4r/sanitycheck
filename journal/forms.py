from django import forms

# forms
class InteractionForm(forms.Form):
    your_title = forms.CharField(max_length=30)
    your_convo = forms.CharField()
    # your_date = forms.DateTimeField()