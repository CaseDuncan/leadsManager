from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.TextField()
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
