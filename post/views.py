from django.shortcuts import render, get_object_or_404

from post.models import Post
from . import models
# Create your views here.
def home(request):
    posting = Post.objects.order_by('-pub_date')
    #text = Post.objects.order_by('text')
    return render(request,'post/home.html',{'latest_post':posting})

def post_sp(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', {'post_id':post})
