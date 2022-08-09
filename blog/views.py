from django.shortcuts import render
from django.views import generic, View
from .models import BlogPost, BlogPostCategory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
# Create your views here.



def blog(request):
    """ A view to return the blog"""
    categories = BlogPostCategory.objects.all()
    posts = BlogPost.objects.all()

    

    return render(request, 'blog/blogindex.html', {'categories': categories, 'posts': posts})


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
    context = {"blog_category_list": blog_category_list, }
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
    template_name = "blog/blog_post_detail.html"

class BlogPostCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new blogpost """
    model = BlogPost
    """ Pass in all fields except post author"""
    fields = ['title', 'post_text', 'category']
    template_name = "blog/blog_post_form.html"
    success_url = reverse_lazy('blog')

class BlogPostDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ Delete a post from the site"""
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog')


def add_category(request):
    name = request.POST.get('categoryname')
    
    # add category
    category = BlogPostCategory.objects.get_or_create(name=name)[0]
    
   
    if not BlogPostCategory.objects.filter(name=name).exists():
        BlogPostCategory.objects.create(name=name)

    # return template fragment with all the user's films
    categories = BlogPostCategory.objects.all()

    return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})

@require_http_methods(['DELETE'])
@login_required
def delete_category(request, pk):
    
    # remove the category
    BlogPostCategory.objects.get(pk=pk).delete()

    # return template fragment with all the user's films
    categories = BlogPostCategory.objects.all()
    return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})
