from django.shortcuts import render_to_response
from django.template import RequestContext

from rustic_cut.models import Product, Category


def index(request):
    fp = Product.objects.filter(featured=True).first()
    featured_product = fp if (fp and fp.photo) else None
    context = {
        'featured_product': featured_product
    }
    
    return render_to_response("rustic_cut/html/index.html", context, context_instance=RequestContext(request))


def about(request):
    return render_to_response("rustic_cut/html/about.html", {}, context_instance=RequestContext(request))


def contact(request):
    return render_to_response("rustic_cut/html/contact.html", {}, context_instance=RequestContext(request))


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render_to_response("rustic_cut/html/products.html", context, context_instance=RequestContext(request))


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render_to_response("rustic_cut/html/product.html", context, context_instance=RequestContext(request))
    

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category
    }
    return render_to_response("rustic_cut/html/category.html", context, context_instance=RequestContext(request))