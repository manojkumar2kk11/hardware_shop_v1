from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm

def index(request):
    """ A view to return the index page and handle newsletter form """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed successfully!')
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/index.html', context)


def subscribe(request):
    """ If you want to have a dedicated subscribe page """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed successfully!')
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/subscribe.html', context)