from django.shortcuts import render, redirect
from django.contrib import messages
from .models import fit_Profile


def load_profile_builder (request):
    return render(request, 'profile_builder.html')

def build_profile(request):
    results = fit_Profile.objects.buildProfile(request.POST)
    messages.success(request, "Thanks for completing your fit_Profile!")
    return redirect('/dashboard')

def load_dashboard(request):
    return render(request, 'dashboard.html')

def load_workout_tree(request):
    return render(request, 'workout_tree.html')

def load_workout_education_base(request):
    return render(request, 'workout_education_base.html',)

# def load_calisthenics_page(request):
#     return render(request, 'calisthenics_page.html')
    
# def load_endurance_training_page(request):
#     return render(request, 'endurance_training_page.html')




