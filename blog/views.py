from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Post

def post_list(request):
    #return HttpResponseNotFound('<h1>Page not found</h1>')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
