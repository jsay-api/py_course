from django.shortcuts import render, render_to_response

from models import Post
# Create your views here.

def posts(request):
    post_list = Post.objects.all()
    
    return render_to_response('spaceblog/post_list.html', {'post_list':post_list})
    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    
    return render_to_response('spaceblog/post_detail.html', {'post':post})    