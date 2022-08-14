from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.db.models import Avg
from django.http import HttpResponse
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm
from profiles.models import WishlistItem
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.


def all_products(request):
    """ A view to return the products page """
    sorted_products = Product.objects.all()
    sorted_products = sorted_products.order_by("price")

    return render(request, 'products/products.html',
                  {"sorted_products": sorted_products, "category": None})


def category_products(request, category):
    """ A view to return the products by category page """
    newcat = category
    sorted_products = Product.objects.filter(category__name=newcat)
    sorted_products = sorted_products.order_by("price")

    return render(request,
                  'products/category_view.html',
                  {"sorted_products": sorted_products,
                   "product_category": category})


def products_ranking(request):
    """ A view to show all products, including sorting  """

    sorted_products = Product.objects.all()
    sortkey = request.GET['ranking']
    sorted_products = sorted_products.order_by("price")

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        sorted_products = sorted_products.filter(category__name__in=categories)

    if sortkey == "price_asc":
        sorted_products = sorted_products.order_by("price")
    if sortkey == 'price_desc':
        sorted_products = sorted_products.order_by("-price")

    if sortkey == "name_asc":
        sorted_products = sorted_products.order_by("name")
    if sortkey == 'name_desc':
        sorted_products = sorted_products.order_by("-name")

    if sortkey == "rating_asc":
        sorted_products = sorted_products.order_by("rating")
    if sortkey == 'rating_desc':
        sorted_products = sorted_products.order_by("-rating")

    return render(request, 'products/snippets/product_list.html',
                  {"sorted_products": sorted_products})


class ProductCategoryList(generic.ListView):
    """Takes GET request, returns products by category"""
    model = Product
    template_name = "blog/categoryindex.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Product.objects.filter(
                category__name=self.kwargs['category'])}
        return content


@staff_member_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@staff_member_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return HttpResponse("")


def htmx_search_products(request):
    """ Search function for live HTMX search"""
    products = Product.objects.all()
    query = None
    query = request.POST.get('q')
    queries = Q(name__icontains=query) | Q(description__icontains=query)
    products = products.filter(queries)
    context = {"products": products}

    return render(request, 'products/includes/search_results.html', context)


def search_page(request):
    """ A view to return the search page """

    return render(request, 'products/search.html')


def product_detail(request, product_id):
    """ A view to show individual product details and handle comments """
    product = get_object_or_404(Product, pk=product_id)
    # checks to see if product on user wishlist to set initial button state
    added = False
    if request.user.is_authenticated:
        if WishlistItem.objects.filter(
                author=request.user,
                product=product).count() > 0:
            added = True
    # handle comment form
    new_comment = None
    # Comment received
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    # clear form
    comment_form = CommentForm()
    context = {
        'product': product,
        'added': added,
        'comment_form': comment_form,
    }

    return render(request, 'products/product_detail.html', context)


def product_category_list(request):
    """ Creates a list of categories to be used by dropdown menu"""
    product_category_list = Category.objects.all()
    context = {"product_category_list": product_category_list, }
    return context


@login_required
def add_to_wishlist(request, id):
    try:
        product = Product.objects.get(id=id)
    except BaseException:
        """If not, return to the wishlist page """
        return redirect(reverse('products'))

    if WishlistItem.objects.filter(author=request.user,
                                   product=product).count() > 0:
        WishlistItem.objects.filter(author=request.user,
                                    product=product).delete()
        return render(
            request,
            'products/includes/wishlist_snippet.html',
            context={
                'product': product,
                'added': False})

    """ Create the wishlist item and return the user to wishlist page"""
    WishlistItem.objects.create(author=request.user, product=product)
    return render(
        request,
        'products/includes/wishlist_snippet.html',
        context={
            'product': product,
            'added': True})


@login_required
def delete_wishlist_item(request, id):
    """ remove wishlist object"""
    wish = get_object_or_404(WishlistItem, pk=id)
    if wish.author.id == request.user.id:
        wish.delete()
        # empty HTML string for table
        return HttpResponse("")

    else:
        return redirect('home')
        messages.error(request, 'You do not have permission to do this')


@staff_member_required
def add_product_category(request):
    """ Add new category """
    name = request.POST.get('categoryname')
    # add category
    category = Category.objects.get_or_create(name=name)[0]
    if not Category.objects.filter(name=name).exists():
        Category.objects.create(name=name)
    categories = Category.objects.all()

    return render(request,
                  'products/snippets/categories_list.html',
                  {'categories': categories})


@staff_member_required
def edit_product_category(request, id):
    """ edit catgeory for product """
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        if request.POST.get('newname') == '':
            return render(request,
                          'products/snippets/categories_item.html',
                          {'category': category})
        else:
            category.name = request.POST.get('newname')

        category.save()
        product_category_list = Category.objects.all()

        return render(request,
                      'products/snippets/categories_item.html',
                      {'category': category})

    return render(request,
                  'products/snippets/categories_edit.html',
                  {'cat': category})


@require_http_methods(['DELETE'])
@staff_member_required
def delete_product_category(request, id):
    """ delete category"""
    Category.objects.get(pk=id).delete()

    return HttpResponse("")


class ProductCreateView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        generic.CreateView):
    """ Create a new product listing """
    model = Product
    """ Pass in fields"""
    fields = [
        'name',
        'sku',
        'rating',
        'category',
        'description',
        'price',
        'image']
    template_name = "products/product_form.html"
    success_url = reverse_lazy('manage_products')

    def test_func(self):
        return self.request.user.is_staff


class ProductUpdateView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        generic.UpdateView):
    """ CBV to update product listing"""
    model = Product
    template_name = "products/product_form.html"
    fields = [
        'name',
        'sku',
        'rating',
        'category',
        'description',
        'price',
        'image']
    success_url = reverse_lazy('manage_products')

    def test_func(self):
        return self.request.user.is_staff


@login_required
def delete_comment(request, id):
    """ Remove product comment"""
    comment = get_object_or_404(Comment, id=id)
    product = comment.product
    if comment.author == request.user or request.user.is_superuser:
        comment.delete()

    return redirect(reverse_lazy('product_detail', args=(product.id,)))
