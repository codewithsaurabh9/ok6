from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from django.urls import path,include
from django.conf.urls.static import static

from.import views

# from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    path(r'foo/',views.download),





    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)