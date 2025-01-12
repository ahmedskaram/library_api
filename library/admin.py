from django.contrib import admin
from .models import Book, Transaction

##########################################################################################

# Register the Book model in the admin panel
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'copies_available')
    search_fields = ('title', 'author', 'isbn')

# Register the Transaction model in the admin panel
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'checkout_date', 'return_date')
    list_filter = ('checkout_date', 'return_date')
    search_fields = ('user__username', 'book__title')

##########################################################################################
