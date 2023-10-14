from django.db import models

# Create your models here.

class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    seen = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.name}'
