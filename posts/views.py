from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    data = Post.objects.all()  # orm --> sql --> db --> list[all posts]
    return render(request, 'posts.html', {'posts':data})