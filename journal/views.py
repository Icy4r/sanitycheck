from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from journal.models import Interaction
from journal.forms import InteractionForm

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Ian'})

def display_interactions(request):
    all_interactions = Interaction.objects.all()
    context = {
        'interactions': all_interactions
    }
    return render(request, 'journals_page.html', context)

# input the new interaction
def input_interactions(request):
    
    if request.method == 'POST':
        form = InteractionForm(request.POST)

        if form.is_valid():
            # do work with the data
            print('yee')
            title = form.cleaned_data['your_title']
            conversation = form.cleaned_data['your_convo']
            date = form.cleaned_data['your_date']
            i = Interaction(title=title, conversations=conversation, time=date)
            i.save()

            return HttpResponseRedirect("/journal/")
    
    else:
        form = InteractionForm()

    return render(request, 'addInteraction.html', {'form': form})