from django.db import models

class WishlistItem(models.Model):
    items = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.items
