from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Business, Profile, Neighbourhood, News, Health, Authorities
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NewsForm, UpdatebioForm, NewBusinessForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    try:
        if not request.user.is_authenticated:
            return redirect('accounts/login/')
        user = request.user
        profile = Profile.objects.get(username=user)
    except ObjectDoesNotExist:
        return redirect('create_profile')

    return render(request, 'index.html')

def my_profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    return render(request, 'my_profile.html', {"profile": profile})