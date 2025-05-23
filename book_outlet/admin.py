from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    list_filter=('author','title','rating')
    list_display=('title','rating')
admin.site.register(Book, BookAdmin)
