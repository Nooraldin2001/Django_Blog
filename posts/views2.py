from django.views import generic
from .models import Post

class Post_List(generic.ListView):
    model = Post

    # context : post_list, object_list
    # template: post_list.html 

class Post_Detail(generic.DetailView):
    model = Post



