from django.shortcuts import render
from .models import Book
# Create your views here.

def all_book_details(request):
    books=Book.objects.all()
    return render(request,'./book_outlet/index.html',{
        "books": books
    })
    
def book_details(request, book_title):
    book_title = " ".join(word.capitalize() for word in book_title.split("-"))
    try:
        book = Book.objects.get(title=book_title)
    except Book.DoesNotExist:
        book = None
    return render(request, './book_outlet/book_detail.html', {
        'book': book
    })