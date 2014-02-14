from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#from getpizza import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('getpizza.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
