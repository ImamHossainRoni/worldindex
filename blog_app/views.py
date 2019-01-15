from django.shortcuts import render
from .models import Post
# Create your views here.
context ={
    'posts':Post.objects.all()
}
def home(request):
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html',{'title':'about'})