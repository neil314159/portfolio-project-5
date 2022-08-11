from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg

from .models import Product, Category
from .forms import ProductForm
from profiles.models import WishlistItem

# Create your views here.

def all_products(request):
    """ A view to return the dashboard page """
    sorted_products = Product.objects.all()
    return render(request, 'products/products.html', {"sorted_products": sorted_products})

def products_ranking(request):
    """ A view to show all products, including sorting and search queries """

    sorted_products = Product.objects.all()
    sort = None
    direction = None
   
    sortkey = request.GET['ranking']
    
    
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
        
      
    

    return render(request, 'products/snippets/product-list.html', {"sorted_products": sorted_products})


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
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
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
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
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
    return redirect(reverse('products'))

def htmx_search_products(request):
    
    products = Product.objects.all()
    
    
        
    

    products = Product.objects.all()
    query = None
       

    query =  request.POST.get('q')
   
    queries = Q(name__icontains=query) | Q(description__icontains=query)
    products = products.filter(queries)
   
    
    context = {"products": products}
    return render(request, 'products/includes/search-results.html', context)

def search_page(request):
    """ A view to return the dashboard page """

    
    return render(request, 'products/search.html')


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    added = False
    if request.user.is_authenticated:
        if WishlistItem.objects.filter(author=request.user, product=product).count() > 0:
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
        return render( request, 'products/includes/wishlist-snippet.html', context={'product':product, 'added': False})

    

    """ Create the wishlist item and return the user to wishlist page"""
    WishlistItem.objects.create(author=request.user, product=product)
    return render( request, 'products/includes/wishlist-snippet.html', context={'product':product, 'added': True})
    


    # if request.method == "POST":
    #     instance = Product.objects.get(id=id)
    #     if not instance.likes.filter(id=request.user.id).exists():
    #         instance.likes.add(request.user)
    #         instance.save() 
    #         return render( request, 'posts/partials/likes_area.html', context={'post':instance})
    #     else:
    #         instance.likes.remove(request.user)
    #         instance.save() 
    #         return render( request, 'posts/partials/likes_area.html', context={'post':instance})