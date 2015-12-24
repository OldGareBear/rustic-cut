from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response("rustic_cut/html/index.html", {}, context_instance=RequestContext(request))


def about(request):
    return render_to_response("rustic_cut/html/about.html", {}, context_instance=RequestContext(request))


def contact(request):
    return render_to_response("rustic_cut/html/about.html", {}, context_instance=RequestContext(request))


def products(request):
    return render_to_response("rustic_cut/html/products.html", {}, context_instance=RequestContext(request))
