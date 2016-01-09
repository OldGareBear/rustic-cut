import json
import logging

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from rustic_cut.models import Product, Category
from rustic_cut.forms import ContactForm


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
    context = {
        "contact_form": ContactForm()
    }
    return render_to_response("rustic_cut/html/contact.html", context, context_instance=RequestContext(request))


def contact_submit(request):

    try:
        if not request.method == 'POST':
            raise Exception("Invalid Protocol")

        contact_form = ContactForm(request.POST)
        if not contact_form.is_valid():
            raise Exception("Validation Error")

        user_email = contact_form.cleaned_data["email"]
        message = contact_form.cleaned_data["message"]
        name = contact_form.cleaned_data["name"]
        full_email = name + "<" + user_email + ">"

        send_mail("A message from %s %s" % (name, full_email), message, user_email,  ['rusticcutwoodworking@gmail.com'])

        response = {
            'status': 'ok',
            'message': "Thank you for reaching out to us, we will get back to you as soon as possible."
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
    # if not request.method == 'POST':
    #     raise Exception("Invalid Protocol")
    #
    # contact_form = ContactForm(request.POST)
    # if not contact_form.is_valid():
    #     raise Exception("Validation Error")
    #
    # user_email = contact_form.cleaned_data["email"]
    # message = contact_form.cleaned_data["message"]
    # name = contact_form.cleaned_data["name"]
    # full_email = name + "<" + user_email + ">"
    #
    # send_mail("A message from %s %s" % (name, full_email), message, user_email,  ['rusticcutwoodworking@gmail.com'])
    #
    # response = {
    #     'status': 'ok',
    #     'message': "Thank you for reaching out to us, we will get back to you as soon as possible."
    # }
    # return HttpResponse(json.dumps(response), content_type="application/json")
        

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
    products = Product.objects.filter(id=category_id)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render_to_response("rustic_cut/html/products.html", context, context_instance=RequestContext(request))