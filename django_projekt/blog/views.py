from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'BlogPost1',
        'content': 'First post content',
        'date_posted': 'Grudzień 21, 2020'
    },
    {
        'author': 'Jane doe',
        'title': 'BlogPost2',
        'content': 'second post content',
        'date_posted': 'Grudzień 21, 2020'
    }

]


def home(request):
    context  = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})