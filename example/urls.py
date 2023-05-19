from django.urls import path
from .views import (
    square_numbers,
    add_two_numbers
)
urlpatterns = [
    path('square-numbers/', square_numbers, name='square_numbers'),
    path('add-two-numbers/', add_two_numbers, name='load_test_endpoint'),
]

