from django.urls import path

from . import views

urlpatterns = [
    path('login', views.authenticate_user, name='LoginUser'),
    path('category', views.category, name='Category'),
    path('shop', views.shop, name='Shop'),
    path('item', views.item, name='Item'),
]
