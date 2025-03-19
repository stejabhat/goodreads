from rest_framework import viewsets, permissions
from .models import Book, ReadingList
from .serializers import BookSerializer, ReadingListSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class ReadingListViewSet(viewsets.ModelViewSet):
    queryset = ReadingList.objects.all()  # Explicitly define queryset
    serializer_class = ReadingListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
