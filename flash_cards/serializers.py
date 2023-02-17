from rest_framework import serializers
from .models import FlashCard

class FlashCardSerializer(serializers.ModelsSerializer):
    class Meta: 
        model = FlashCard
        fields = '__all__'

        