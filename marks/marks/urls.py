from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marks.views.home', name='home'),
    # url(r'^marks/', include('marks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'index.html'}),
   # url(r'^$', 'django.views.generic.simple.direct_to_template', 'webmarks.views.lastMarkList'),
    url(r'^$','webmarks.views.markindex'),
    
    #
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
