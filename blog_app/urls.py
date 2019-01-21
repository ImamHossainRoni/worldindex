from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .import views
urlpatterns = [
    path('',PostListView.as_view(),name = 'home-view'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'detail-view'),
    path('post/new/',PostCreateView.as_view(),name = 'create-view'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'update-view'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'delete-view'),
    path('about',views.about,name = 'about-view'),
]
