from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_book_details, name='all_book_details'),
    path("<str:book_slug>", views.book_details, name='book_details')
]