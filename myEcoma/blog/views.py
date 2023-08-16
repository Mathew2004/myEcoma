from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    post = Blogpost.objects.all()

    return render(request, 'blog/index.html', {'post':post})



def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)
    mypost = Blogpost.objects.all()
    print(post[0])
    content = {'post': post[0], 'mypost':mypost}

    return render(request,'blog/blogpost.html',content)