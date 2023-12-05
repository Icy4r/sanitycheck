from django import forms
from django.contrib.admin.widgets import AdminDateWidget

# forms
class InteractionForm(forms.Form):
    your_title = forms.CharField(label='Title', max_length=30)
    your_convo = forms.CharField(label='Conversation')
    your_date = forms.DateField(label= "Date", widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))