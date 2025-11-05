from django.shortcuts import render

def handler404(request, exception=None):
    """Custom 404 handler used by Django when DEBUG=False."""
    return render(request, "404.html", status=404)