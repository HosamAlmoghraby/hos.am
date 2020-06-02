from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Portfolio Admin Area'
admin.site.site_title = 'Portfolio'
admin.site.index_title = 'Home Administration'


urlpatterns = [
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('wedding/', include('wedding.urls')),
    path('idarah/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
