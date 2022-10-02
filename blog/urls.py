# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for the blog which shows all posts and post expand which
# enters the post for the user to read
urlpatterns = [
    path('blog/', views.PublishedPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.PostExpand.as_view(), name='post_expand'),
]
