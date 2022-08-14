
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import BlogPost, BlogPostCategory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here.


def blog(request):
    """
    A view to return the blog
    """
    posts = BlogPost.objects.all()

    return render(request, 'blog/blogindex.html', {'posts': posts})


class BlogCategoryList(generic.ListView):
    """
    Takes GET request, returns articles by category
    """
    model = BlogPostCategory
    template_name = "blog/categoryindex.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects.filter(
                category__name=self.kwargs['category'])}
        return content


def blog_category_list(request):
    """
    Creates a list of categories to be used by dropdown menu in navbar
    """
    blog_category_list = BlogPostCategory.objects.all()
    context = {"blog_category_list": blog_category_list, }
    return context


class BlogPostDetail(generic.DetailView):
    """
    Class based view passing to template, form is automatically generated
    """
    model = BlogPost
    template_name = "blog/blog_post_detail.html"


class BlogPostCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Create a new blogpost
    """
    model = BlogPost
    """ Pass in all fields except post author"""
    fields = ['title', 'category', 'image', 'post_text']
    template_name = "blog/blog_post_form.html"
    success_url = reverse_lazy('blog')


class BlogPostUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Edit a published post
    """
    model = BlogPost
    template_name = "blog/blog_post_form.html"
    fields = ['title', 'category', 'image', 'post_text']


class BlogPostDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Delete a post from the site
    """
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog')


@login_required
def delete_blog_post(request, id):
    """
    Delete a blog post
    """
    blogpost = get_object_or_404(BlogPost, pk=id)
    if request.user.is_superuser:
        blogpost.delete()
        posts = BlogPost.objects.all()
        # returns empty html string to be inserted in table by HTMX
        return HttpResponse("")
    else:
        return redirect('home')
        messages.error(request, 'You do not have permission to do this')


def add_category(request):
    """
    Add a new blog category via HTMX
    """
    name = request.POST.get('categoryname')
    # add category
    category = BlogPostCategory.objects.get_or_create(name=name)[0]
    if not BlogPostCategory.objects.filter(name=name).exists():
        BlogPostCategory.objects.create(name=name)
    categories = BlogPostCategory.objects.all()

    return render(request,
                  'blog/snippets/categories_list.html',
                  {'categories': categories})


@require_http_methods(['DELETE'])
@login_required
def delete_category(request, pk):
    """
    Remove category and send back empty string to replace entry in table
    """
    BlogPostCategory.objects.get(pk=pk).delete()

    return HttpResponse("")


def edit_category(request, id):
    """
    edit category and return snippet with updated name
    """
    blogcat = get_object_or_404(BlogPostCategory, id=id)
    if request.method == 'POST':
        if request.POST.get('newname') == '':
            return render(request,
                          'blog/snippets/categories_item.html',
                          {'category': blogcat})
        else:
            blogcat.name = request.POST.get('newname')
        blogcat.save()
        blog_category_list = BlogPostCategory.objects.all()

        return render(request,
                      'blog/snippets/categories_item.html',
                      {'category': blogcat})

    return render(request,
                  'blog/snippets/categories_edit.html',
                  {'cat': blogcat})


def categories_table(request):
    """
    Provide table of all blog categories in snipett
    """
    categories = BlogPostCategory.objects.all()

    return render(request,
                  'blog/HTMXsnippets/categories_table.html',
                  {'categories': categories})
