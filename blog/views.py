from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

'''login required mixin is used so that we will able to access the page only if its logged in 
User passes test mixin is used for checking some test condition for users to visit a certain page 
in here only the author who have written the blog can update it '''
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    '''to make the ordering from newest to oldest'''
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    '''overding the form during submision so that new blog will be created on any of the author '''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    '''overding the form during submision so that new blog will be created on any of the author '''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    '''test_func is a boolean function based on the return value we will be able to update the post'''

    def test_func(self):
        ''' will return the post that we r curently going to acces'''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
