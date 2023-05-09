from django.urls import path
from .views import index, read, create, delete, update

urlpatterns = [
    path('', index),
    path('read/<id>/', read),
    path('update/<id>/', update),
    path('create/', create),
    path('delete/', delete)
]
