from django.shortcuts import render
from django.http import HttpResponse

def handler404(request, exception=None):
    """Custom 404 handler used by Django when DEBUG=False."""
    try:
        return render(request, "404.html", status=404)
    except Exception:
        # Minimal safe fallback to prevent 500s if template or includes fail
        return HttpResponse(
            "<!doctype html><html><head><title>404 Not Found</title></head>"
            "<body style=\"font-family: Lato, Arial, sans-serif; background:#f8f9fa; color:#343a40;\">"
            "<div style=\"max-width:720px;margin:4rem auto;padding:2rem;background:#fff;border:1px solid #eee;\">"
            "<h1 style=\"margin-top:0;\">Page not found (404)</h1>"
            "<p>Sorry, the page you requested was not found.</p>"
            "<p><a href=\"/\" style=\"color:#0056b3;\">Return home</a></p>"
            "</div></body></html>",
            status=404,
            content_type="text/html",
        )