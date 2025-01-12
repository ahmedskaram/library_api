from rest_framework import viewsets, serializers
from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated

##########################################################################################

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

##########################################################################################

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.copies_available <= 0:
            raise serializers.ValidationError("This book is not available for checkout.")
        book.copies_available -= 1
        book.save()
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.return_date:
            book = instance.book
            book.copies_available += 1
            book.save()

##########################################################################################
