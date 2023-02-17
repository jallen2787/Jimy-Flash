from rest_framework import viewsets

from .serializers import FlashCardSerializer
from .models import FlashCard

class FlashCardViewSet (viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

