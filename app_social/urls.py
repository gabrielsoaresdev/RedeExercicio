from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^persons/$', persons),
    url(r'^persons/add/$', add_persons),
    url(r'^persons/(?P<person_id>.*)/edit/$', edit_person)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
