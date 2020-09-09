from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('root.urls')),
    path('content/',include('content.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
