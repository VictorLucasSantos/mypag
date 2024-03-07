from django.urls import path

from mypag.blog import views

urlspatterns = [
    path('', views.PostViews.as_view(), name='home')
]