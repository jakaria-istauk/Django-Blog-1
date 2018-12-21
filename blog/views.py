from django.shortcuts import render

posts = [
    {
        'author': 'Jakaria',
        'title': 'Blog Post 1',
        'content': 'Firsst post content',
        'date_posted': 'Agust 28, 2018'
    },
    {
        'author': 'Istauk',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Agust 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

