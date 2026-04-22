# ULTIMATE GUIDE: Fixing Google Login (Django + Allauth)

---

## Overview

This guide walks you through setting up Google authentication in a Django application using django-allauth. It includes step-by-step instructions and troubleshooting based on real issues encountered during setup.

---

## Step 1: Start Your Django Server

Open VS Code and open your project folder:

cd_spec_viewer_web

Open a terminal:

Terminal → New Terminal

Run the server:

python3 manage.py runserver

You should see:

Starting development server at http://127.0.0.1:8000/

Open this in your browser:

http://127.0.0.1:8000/

---

## Step 2: Access Django Admin

Go to:

http://127.0.0.1:8000/admin

If you do NOT have an admin account, create one:

python3 manage.py createsuperuser

You will be prompted to enter:
- Username
- Email
- Password

After creating the account, log into the admin page.

---

## Step 3: Configure Sites (VERY IMPORTANT)

Inside Django Admin:

1. Click Sites  
2. Click the existing site (usually example.com)  
3. Update the fields:

Domain name → 127.0.0.1:8000  
Display name → Local Development  

4. Click Save  

This step is critical — it tells Django what domain your app is running on.

---

## Step 4: Create Google OAuth Client

Go to:

https://console.cloud.google.com/

Navigate to:

APIs & Services → Credentials

If prompted: Configure OAuth Consent Screen  
- Choose External  
- Fill out required fields (app name, email)  
- Add your email as a Test User  
- Save and continue  

Create OAuth Client:

Create Credentials → OAuth Client ID  

Set:

Application type → Web application  
Name → Google Login  

Authorized JavaScript Origins:

http://127.0.0.1:8000

Authorized Redirect URIs:

http://127.0.0.1:8000/accounts/google/login/callback/

IMPORTANT: Must match EXACTLY (including http, port, and trailing slash)

Click Create

A popup will appear showing:
- Client ID  
- Client Secret  

COPY BOTH — you will need them next

---

## Step 5: Add Social Application in Django

Go back to Django Admin:

Social Applications → Add Social Application

Fill out EXACTLY:

Provider → Google  
Provider ID → (leave blank)  
Name → Google Login  
Client ID → paste from Google Cloud  
Secret key → paste from Google Cloud  
Key → (leave blank)  
Settings → {}  

Sites Section:

Move 127.0.0.1:8000 → Chosen Sites

Click Save

This connects Django to your Google OAuth credentials.

---

## Step 6: Test Google Login

Go to:

http://127.0.0.1:8000/accounts/login/

Click:

Google

Log in with your Google account.

Expected Result:
- You are redirected back to your site  
- You are logged into Django  

---

## TROUBLESHOOTING

401 deleted_client  
Cause: Old or deleted OAuth client  
Fix: Create a NEW OAuth client and update Django  

redirect_uri_mismatch  
Cause: Redirect URI does not match exactly  
Fix: Ensure exact match including http, port, and trailing slash  

Works locally but not production  
Cause: Different environments  
Fix: Production requires separate setup and access  

Admin login fails  
Cause: User not created in this environment  
Fix: Run python3 manage.py createsuperuser  

SSH fails  
Cause: No server access  
Fix: Contact administrator  

No Social Application  
Fix: Create one in Django admin  

App not verified  
Fix: Add your email as a test user in Google Cloud  

Wrong domain  
Fix: Use 127.0.0.1 consistently  

---

## Important Notes

Local environment is separate from production. Fixing localhost does not fix the deployed site. OAuth credentials are environment-specific.

---

## Summary

You completed:
- Django setup  
- Google OAuth setup  
- Site configuration  
- Social application linking  
- Login testing  

Google authentication is now correctly integrated.