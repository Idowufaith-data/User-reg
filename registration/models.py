from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Welcome(models.Model):
    
    class Meta:
        verbose_name_plural = 'Welcomes'
        verbose_name = 'Welcome'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name