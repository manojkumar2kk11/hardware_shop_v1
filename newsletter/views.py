import hashlib
import json
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm

def mailchimp_subscribe(email, first_name="", last_name=""):
    """
    Subscribe a user to Mailchimp audience. Returns (success: bool, response_json)
    """
    api_key = settings.MAILCHIMP_API_KEY
    list_id = settings.MAILCHIMP_AUDIENCE_ID
    if not api_key or not list_id:
        return False, {"detail": "Mailchimp credentials not configured."}

    # data center from API key 'xxxxx-us3' -> 'us3'
    try:
        dc = api_key.split('-')[-1]
    except Exception:
        return False, {"detail": "Invalid API key format."}

    url = f"https://{dc}.api.mailchimp.com/3.0/lists/{list_id}/members"
    payload = {
        "email_address": email,
        # "status": "subscribed"  # immediate subscribe (use carefully)
        "status": "pending",      # triggers double opt-in email (safer)
        "merge_fields": {
            "FNAME": first_name,
            "LNAME": last_name,
        }
    }

    # Basic auth: username can be any string, password is the API key
    try:
        resp = requests.post(url, auth=("anystring", api_key), json=payload, timeout=10)
        data = resp.json()
        if resp.status_code in (200, 201):
            return True, data
        else:
            # Mailchimp returns useful error messages in JSON
            return False, data
    except requests.RequestException as e:
        return False, {"detail": str(e)}

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            fname = form.cleaned_data.get("first_name", "")
            lname = form.cleaned_data.get("last_name", "")

            ok, response = mailchimp_subscribe(email, fname, lname)
            if ok:
                # success - show message or redirect
                messages.success(request, "Thanks — check your email to confirm subscription.")
                return redirect('newsletter:signup')
            else:
                # Mailchimp error -> show message to user
                # extract meaningful text if available
                err = response.get("detail") or response.get("title") or "Subscription failed."
                messages.error(request, f"Could not subscribe: {err}")
    else:
        form = SignupForm()

    return render(request, "newsletter/signup.html", {"form": form})
