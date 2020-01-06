from django.db import models
from django.utils import timezone

# Create your models here.
class StationAdmin(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    registerTime = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", blank=True, null=True)
    
    class Meta:
        ordering = ('number',)
        index_together = (('id', 'name', 'email'),)
        
    def __str__(self):
        return self.name
