from django.urls import path
from .views import property_list, favourite_list_create, favourite_delete

urlpatterns = [
    path('', property_list),
    path('favourites/', favourite_list_create),
    path('favourites/<int:pk>/', favourite_delete),
]