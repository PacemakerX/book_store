from django.shortcuts import render
from .models import Book
# Create your views here.

def all_book_details(request):
    books=Book.objects.all()
    return render(request,'./book_outlet/index.html',{
        "books": books
    })
    
def book_details(request, book_slug):
    try:
        book = Book.objects.get(slug=book_slug)
    except Book.DoesNotExist:
        book = None
    return render(request, './book_outlet/book_detail.html', {
        'book': book
    })