from django.shortcuts import render
from .models import Post
# Create your views here.
posts = [
    {
        'author' : 'Imam',
        'title'  : 'Blog post-1',
        'content': 'first blog post',
        'date_posted' : '20 august,2018'
    },
    {
        'author' : 'Al Sweigart',
        'title'  : 'Blog post-2',
        'content': 'Second blog post',
        'date_posted' : '22 august,2018'
    }
]
context ={
    'posts':Post.objects.all()
}
def home(request):
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html',{'title':'about'})