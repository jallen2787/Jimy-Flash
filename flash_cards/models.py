from django.db import models

class FlashCard(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    