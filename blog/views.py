# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PublishedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog.html'
    paginated_by = 6

    def get(self, request, *args, **kwargs):
        """
        This view renders the blog page and also all published posts
        """
        posts = Post.objects.all()
        return render(request, 'blog/blog.html',  {'posts': posts})


class PostExpand(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by('-created_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 'blog_expand.html',
            {'post': post,
             'comments': comments,
             'liked': liked},
        )
