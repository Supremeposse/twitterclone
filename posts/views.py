from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.erros.as_json())

    posts = Post.objects.all()[:20:-1]

    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
	if request.method == "GET":
		edittweet=Post.objects.get(id = post_id)
	if request.method == "POST":
		edittweet = Post.objects.get(id=post_id)
		form = PostForm(request.POST,request.FILES,instance=edittweet)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse("not valid")

	return render (request,'edit.html',{"edittweet":edittweet})

def likes(request, post_id):
    likedtweet = Post.objects.get(id = post_id)
    likedtweet.like_count += 1
    likedtweet.save()
    return HttpResponseRedirect('/#'+str(post_id))