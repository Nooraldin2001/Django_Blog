from django.views import generic
from .models import Post

class Post_List(generic.ListView):
    model = Post

    # context : post_list, object_list
    # template: post_list.html 

class Post_Detail(generic.DetailView):
    model = Post


class Add_Post(generic.CreateView):
    model = Post
    fields = ['author','title', 'content', 'tags', 'img']
    success_url = '/blog/'

class Edit_Post(generic.UpdateView):
    model = Post
    fields = ['author','title', 'content', 'tags', 'img']
    success_url = '/blog/'
    template_name = 'posts/Edit_Post.html'

class Delete_Post(generic.DeleteView):
    model = Post
    success_url = '/blog/'









