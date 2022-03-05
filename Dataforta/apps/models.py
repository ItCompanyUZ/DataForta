from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=50)
    theme = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kelgan Izoxlar'
        verbose_name_plural = 'Kelgan Izoxlar'

    def __str__(self):
        return self.name

