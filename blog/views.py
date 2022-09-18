# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PublishedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):
        """

        """
        return render(request, 'blog/blog.html')