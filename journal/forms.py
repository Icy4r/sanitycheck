from django import forms
from django.contrib.admin.widgets import AdminDateWidget

# forms
class InteractionForm(forms.Form):
    your_title = forms.CharField(label='Title', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    your_convo = forms.CharField(label='Conversation', widget=forms.Textarea(attrs={'class': 'form-control'}))
    your_date = forms.DateField(label= "Date", widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))