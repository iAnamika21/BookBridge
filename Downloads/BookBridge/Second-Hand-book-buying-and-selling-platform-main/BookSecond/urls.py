
from django.contrib import admin
from django.urls import path, include
from book_store import views
from django.urls import re_path
from . import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_store.urls')),
    re_path(r'^$', views.index, name='index'),
    path('captcha',include('captcha.urls')),
    re_path('viewp/<int:myid', views.single, name='single_product')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
