from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status='Draft').order_by('-created_on')
    template_name = 'index.html'
    
    
    
class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'