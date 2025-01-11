from rest_framework.response import Response
from rest_framework.decorators import action

class TransactionViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def checkout(self, request):
        user = request.user
        book_id = request.data.get('book_id')
        book = Book.objects.get(id=book_id)

        if book.copies_available > 0:
            Transaction.objects.create(user=user, book=book)
            book.copies_available -= 1
            book.save()
            return Response({'message': 'Book checked out successfully!'})
        return Response({'error': 'No copies available!'}, status=400)

    @action(detail=False, methods=['post'])
    def return_book(self, request):
        user = request.user
        transaction_id = request.data.get('transaction_id')
        transaction = Transaction.objects.get(id=transaction_id, user=user)

        if transaction and not transaction.return_date:
            transaction.return_date = timezone.now()
            transaction.save()
            transaction.book.copies_available += 1
            transaction.book.save()
            return Response({'message': 'Book returned successfully!'})
        return Response({'error': 'Invalid transaction!'}, status=400)
