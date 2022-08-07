from django.shortcuts import render
from django.views import generic, View
from .models import BlogPost, BlogPostCategory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
# Create your views here.



def blog(request):
    """ A view to return the blog"""

    return render(request, 'blog/blogindex.html')


class BlogCategoryList(generic.ListView):
    """Takes GET request, returns articles by category"""
    model = BlogPostCategory
    template_name = "category.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects
            .filter(category__name=self.kwargs['category'])
        }
        return content


def blog_category_list(request):
    """ Creates a list of categories to be used by dropdown menu"""
    blog_category_list = Category.objects.all()
    context = {"review_category_list": review_category_list, }
    return context


class BlogPostList(generic.ListView):
    """ Return a listview of all posts, ordered by date and paginated """
    model = BlogPost
    queryset = BlogPost.objects.order_by("-published_on")
    paginate_by = 4
    template_name = "blog/blogpostlist.html"


class BlogPostDetail(generic.DetailView):
    """Class based view passing to template, form is automatically generated"""
    model = BlogPost
    template_name = "blog_post_detail.html"

class BlogPostCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new blogpost """
    model = Review
    """ Pass in al fields except post author"""
    fields = ['title', 'post_text', 'category']
    template_name = "blog_post_form.html"