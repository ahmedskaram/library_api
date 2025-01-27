from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TransactionViewSet

##########################################################################################

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls

##########################################################################################