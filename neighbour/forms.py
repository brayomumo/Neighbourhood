from django import forms
from .models import News, Business, Profile, Authorities


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['author', 'neighbourhood', 'post_date']


class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username', ]


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']
