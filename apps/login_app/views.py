from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def load_login_page (request):
    return render(request, 'index.html')

def create_account (request):
    User.objects.createUser(request.POST)
    messages.success(request, "You made an account. Sweeet.")
    return redirect('/')

def login (request):
    results = User.objects.retrieveUser(request.GET)
    
    if results['status'] == False:
        for error in results['erros']:
            messages.success(request,error)
        return redirect('/')

    else:
        messages.success(request, "ACCOUNT RETRIEVED")
        request.session['name'] = results['retrieved_User'].name
        request.session['username'] = results['retrieved_User'].username
        request.session['id'] = results['retrieved_User'].id

        return redirect('/main')
