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


def create_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form})


def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES,
                             instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = UpdatebioForm()
    return render(request, 'edit_profile.html', {"form": form})


def businesses(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    business = Business.objects.filter(neighbourhood_id=profile.neighbourhood)
    return render(request, 'business.html', {'business': business})


def new_business(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == "POST":
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = NewBusinessForm()

    return render(request, 'new_business.html', {"form": form})


def health(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(
        neighbourhood_id=profile.neighbourhood)

    return render(request, 'health.html', {"healthservices": healthservices})


def authorities(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(
        neighbourhood_id=profile.neighbourhood)

    return render(request, 'authorities.html', {"authorities": authorities})


def news(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    news = News.objects.filter(neighbourhood_id=profile.neighbourhood)

    return render(request, 'news.html', {"news": news})


def new_news(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = current_user
            news.neighbourhood_id = profile.neighbourhood
            news.save()

        return HttpResponseRedirect('/news')

    else:
        form = NewsForm()

    return render(request, 'new_news.html', {"form": form})


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        business = request.GET.get("name")
        searched_business = Business.search_by_business(business)
        message = f"{business}"

        return render(request, 'search.html', {"message": message, "news": searched_news})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
