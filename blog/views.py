from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import  timezone
from .models import post
from  django.shortcuts import redirect
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = post.objects.filter(publioshed_date__lte=timezone.now()).order_by('publioshed_date')
    return  render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    postc = get_object_or_404(post, pk=pk)
    post.objects.get(pk=pk)
    return  render(request, 'blog/post_detail.html', {'postc':postc})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)

        else:
            form = PostForm()
            return  render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    postb = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=postb)
        if form.is_valid():
            postb = form.save(commit=False)
            postb.author = request.user
            postb.save()
            return  redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
            return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = post.objects.filter(publioshed_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    postd = get_object_or_404(post, pk=pk)
    postd.publish()
    return redirect('post_detail', pk=post.pk)

def publish(self):
    self.publioshed_date = timezone.now()
    self.save()

def post_remove(request, pk):
    poste = get_object_or_404(post, pk=pk)
    post.delete()
    return redirect('post_list')