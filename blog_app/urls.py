from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name = 'home-view'),
    path('about',views.about,name = 'about-view'),
]
