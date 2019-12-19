from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('recipies.urls')),
    path('', include('categories.urls')),
]
