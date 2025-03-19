from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReadingListViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  
router.register(r'reading-list', ReadingListViewSet, basename='readinglist')

urlpatterns = [
    path('', include(router.urls)),  # Ensure this is correct
]
