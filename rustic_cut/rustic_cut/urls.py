from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rustic_cut.views.index', name='rustic_cut_index'),
    url(r'^$', 'rustic_cut.views.about', name='rustic_cut_about'),
    url(r'^$', 'rustic_cut.views.contact', name='rustic_cut_contact'),
    url(r'^$', 'rustic_cut.views.products', name='rustic_cut_products'),
)
