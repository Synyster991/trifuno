from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    # BASE URLS
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about', views.about, name="about"),
    path('brand', views.brand, name="brand"),
    path('contact', views.contact, name="contact"),
    path('news', views.news, name='news'),
    # SECOND BASE URLS
    path('brand/<int:pk>', views.brand_detail, name='brand_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
