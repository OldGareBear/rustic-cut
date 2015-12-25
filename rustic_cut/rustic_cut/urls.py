from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rustic_cut.views.index', name='rustic_cut_index'),
    url(r'^about/$', 'rustic_cut.views.about', name='rustic_cut_about'),
    url(r'^contact/$', 'rustic_cut.views.contact', name='rustic_cut_contact'),
    url(r'^products/$', 'rustic_cut.views.products', name='rustic_cut_products'),
)\
    + static('/static/', document_root=settings.STATIC_ROOT) \
    + static('/media/', document_root=settings.MEDIA_ROOT)
