from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/', include('app.urls', namespace='v1')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

