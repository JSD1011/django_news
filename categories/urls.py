from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name="indexpage"),
    path('top',views.top,name="toppage"),
    path('trending',views.trending,name="trendingpage"),
    path('science',views.science,name="sciencepage"),
    path('ep',views.ep,name="entretainmentpage"),
    path('sports',views.sports,name="sportspage")
]