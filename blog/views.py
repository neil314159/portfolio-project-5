
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
    # categories = BlogPostCategory.objects.all()
    posts = BlogPost.objects.all()

    

    return render(request, 'blog/blogindex.html', {'posts': posts})


class BlogCategoryList(generic.ListView):
    """Takes GET request, returns articles by category"""
    model = BlogPostCategory
    template_name = "blog/categoryindex.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects.filter(category__name=self.kwargs['category'])
        }
        return content

def blog_category_list(request):
    """ Creates a list of categories to be used by dropdown menu"""
    blog_category_list = BlogPostCategory.objects.all()
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
    fields = ['title', 'post_text', 'category', 'image']
    template_name = "blog/blog_post_form.html"
    success_url = reverse_lazy('blog')

class BlogPostUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ Edit a published review """
    model = BlogPost
    template_name = "post_edit.html"
    fields = ['title', 'book_author', 'review_text', 'category', 'book_cover',
              'purchase_link', 'star_rating']

    

class BlogPostDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ Delete a post from the site"""
    model = BlogPost
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog')

@login_required
def delete_blog_post(request, id):
    
    blogpost = get_object_or_404(BlogPost, pk=id)
    if request.user.is_superuser:
        blogpost.delete()
        # messages.success(request, 'This post is deleted')
        posts = BlogPost.objects.all()
        return render(request, 'blog/HTMXsnippets/posts-list.html', {'posts': posts})
        
    else:
        return redirect('home')
        messages.error(request, 'You do not have permission to do this')


def delete_category(request, pk):
    
    # remove the category
    BlogPostCategory.objects.get(pk=pk).delete()

    # return template fragment with all the categories
    categories = BlogPostCategory.objects.all()
    return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})


def add_category(request):
    name = request.POST.get('categoryname')
    
    # add category
    category = BlogPostCategory.objects.get_or_create(name=name)[0]
    # BlogPostCategory.objects.create(name=name)
   
    if not BlogPostCategory.objects.filter(name=name).exists():
        BlogPostCategory.objects.create(name=name)

    
    categories = BlogPostCategory.objects.all()

    return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})

@require_http_methods(['DELETE'])
@login_required
def delete_category(request, pk):
    
    # remove the category
    BlogPostCategory.objects.get(pk=pk).delete()

    # return template fragment with all the categories
    categories = BlogPostCategory.objects.all()
    return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})

# def edit_category(request, pk):
    
#     # remove the category
#     BlogPostCategory.objects.get(pk=pk).delete()

#     # return template fragment with all the user's films
#     categories = BlogPostCategory.objects.all()
#     return render(request, 'blog/HTMXsnippets/categories-list.html', {'categories': categories})

def student_edit_form(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    context = {'student': student, 'form': form}
    return render(request, 'core/partials/edit-student-form.html', context)

def edit_category(request, id):
   
    blogcat = get_object_or_404(BlogPostCategory, id=id)

    if request.method == 'POST':
        if request.POST.get('newname') == '':
            return render(request, 'blog/HTMXsnippets/categories-item.html', {'category': blogcat})
        else:
            blogcat.name = request.POST.get('newname')
       
        
        blogcat.save()
        blog_category_list = BlogPostCategory.objects.all()

        return render(request, 'blog/HTMXsnippets/categories-item.html', {'category': blogcat})
    
    return render(request, 'blog/HTMXsnippets/categories-edit.html', {'cat': blogcat})

