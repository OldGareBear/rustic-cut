from django.shortcuts import render_to_response
from django.template import RequestContext

from rustic_cut.models import Product


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
    return render_to_response("rustic_cut/html/about.html", {}, context_instance=RequestContext(request))


def products(request):
    return render_to_response("rustic_cut/html/products.html", {}, context_instance=RequestContext(request))
