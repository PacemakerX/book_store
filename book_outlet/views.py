from django.shortcuts import render
from .models import Book
# Create your views here.

def all_book_details(request):
    books=Book.objects.all()
    return render(request,'./book_outlet/index.html',{
        "books": books
    })