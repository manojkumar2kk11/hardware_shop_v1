from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def faq(request):
    """ Frequently Asked Questions page """
    return render(request, 'home/faq.html')


def contact(request):
    """ Contact Us page """
    return render(request, 'home/contact.html')