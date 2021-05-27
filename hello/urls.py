from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^puzzle', views.puzzle),
    url(r'^comment', views.comment, name='comment')
]
