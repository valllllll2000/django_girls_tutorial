from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def post_list(request):
    #return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'blog/post_list.html', {})
