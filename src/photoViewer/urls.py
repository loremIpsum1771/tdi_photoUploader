from django.conf.urls import url
from photoViewer import views
from .views import (home)

urlpatterns = [url(r'^$', home),url(r'^$img', home),]