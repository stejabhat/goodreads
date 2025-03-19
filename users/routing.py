from django.urls import path
from .consumers import ReadingProgressConsumer

websocket_urlpatterns = [
    path("ws/reading-progress/", ReadingProgressConsumer.as_asgi()),
]
