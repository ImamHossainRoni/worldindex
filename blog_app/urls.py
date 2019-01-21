from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)
from .import views
urlpatterns = [
    path('',PostListView.as_view(),name = 'home-view'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'detail-view'),
    path('post/new/',PostCreateView.as_view(),name = 'create-view'),
    path('about',views.about,name = 'about-view'),
]
