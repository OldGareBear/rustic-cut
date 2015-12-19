from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rustic_cut.views.index', 'rustic_cut_index'),
    url(r'^$', 'rustic_cut.views.about', 'rustic_cut_about'),
    url(r'^$', 'rustic_cut.views.contact', 'rustic_cut_contact'),
)
