from django.contrib import admin
from .models import Neighbourhood, Profile, Business, News, Health, Authorities

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(News)
admin.site.register(Health)
admin.site.register(Authorities)