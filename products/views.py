from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm
from profiles.models import WishlistItem
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.


def all_products(request):
    """ A view to return the dashboard page """
    sorted_products = Product.objects.all()
    sorted_products = sorted_products.order_by("price")
    return render(request, 'products/products.html',
                  {"sorted_products": sorted_products})


def category_products(request, category):
    """ A view to return the dashboard page """
    newcat = category
    sorted_products = Product.objects.filter(category__name=newcat)

    sorted_products = sorted_products.order_by("price")
    return render(request,
                  'products/products.html',
                  {"sorted_products": sorted_products,
                   "product_category": category})


def products_ranking(request):
    """ A view to show all products, including sorting and search queries """

    sorted_products = Product.objects.all()
    sort = None
    direction = None

    sortkey = request.GET['ranking']
    sorted_products = sorted_products.order_by("price")

    search = request.GET.get('search')

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
    """Takes GET request, returns articles by category"""
    model = Product
    template_name = "blog/categoryindex.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Product.objects.filter(
                category__name=self.kwargs['category'])}
        return content


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
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


@login_required
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

    products = Product.objects.all()
    query = None

    query = request.POST.get('q')

    queries = Q(name__icontains=query) | Q(description__icontains=query)
    products = products.filter(queries)

    context = {"products": products}
    return render(request, 'products/includes/search_results.html', context)


def search_page(request):
    """ A view to return the dashboard page """

    return render(request, 'products/search.html')


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    added = False
    if request.user.is_authenticated:
        if WishlistItem.objects.filter(
                author=request.user,
                product=product).count() > 0:
            added = True

    context = {
        'product': product,
        'added': added,
    }

    return render(request, 'products/product_detail.html', context)


def product_category_list(request):
    """ Creates a list of categories to be used by dropdown menu"""
    product_category_list = Category.objects.all()
    context = {"product_category_list": product_category_list, }
    return context


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

    wish = get_object_or_404(WishlistItem, pk=id)
    if wish.author.id == request.user.id:
        wish.delete()
        # messages.success(request, 'This post is deleted')

        return HttpResponse("")

    else:
        return redirect('home')
        messages.error(request, 'You do not have permission to do this')

    # if request.method == "POST":
    #     instance = Product.objects.get(id=id)
    #     if not instance.likes.filter(id=request.user.id).exists():
    #         instance.likes.add(request.user)
    #         instance.save()
    #         return render( request, 'posts/partials/likes_area.html', context={'post':instance})
    #     else:
    #         instance.likes.remove(request.user)
    #         instance.save()
    # return render( request, 'posts/partials/likes_area.html',
    # context={'post':instance})


def add_product_category(request):
    name = request.POST.get('categoryname')

    # add category
    category = Category.objects.get_or_create(name=name)[0]
    # BlogPostCategory.objects.create(name=name)

    if not Category.objects.filter(name=name).exists():
        Category.objects.create(name=name)

    # return HttpResponse("")
    categories = Category.objects.all()

    return render(request,
                  'products/snippets/categories_list.html',
                  {'categories': categories})


def edit_product_category(request, id):

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
        # return HttpResponse("here")
        return render(request,
                      'products/snippets/categories_item.html',
                      {'category': category})

    return render(request,
                  'products/snippets/categories_edit.html',
                  {'cat': category})


@require_http_methods(['DELETE'])
@login_required
def delete_product_category(request, pk):

    # remove the category
    Category.objects.get(pk=pk).delete()

    return HttpResponse("")


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new blogpost """
    model = Product
    """ Pass in all fields except post author"""
    fields = ['name', 'sku', 'category', 'description', 'price', 'image']
    template_name = "products/product_form.html"
    success_url = reverse_lazy('manage_products')


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    
    model = Product
    template_name = "products/product_form.html"
    fields = ['name', 'sku', 'category', 'description', 'price', 'image']
    success_url = reverse_lazy('manage_products')
