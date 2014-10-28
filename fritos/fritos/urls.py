from django.conf.urls import patterns, include, url
import settings 
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^usr/', include('usr.urls')),
    url(r'^venta/', include('venta.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
)
 
urlpatterns += patterns('django.views.static',
        (r'static/(?P<path>.*)', 'serve', {'document_root': settings.STATIC_ROOT}),
)