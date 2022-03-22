from django.contrib import admin
from django.urls import URLPattern, path,include
from django.conf import settings
from django.conf.urls.static import static
from app1.views import index
from app1 import views

app_name='app1'
urlpatterns=[
    path('', index),
    path('upload/csv', views.upload_csv, name='upload_csv'),
]
