from django.db import models
from django.conf import settings

# Create your models here.
class Property(models.Model):
    title=models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.TextField
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    

class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favourites')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user} has saved {self.property}"