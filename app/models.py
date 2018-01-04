from django.db import models
from django.utils import timezone


class Coin(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)
    code = models.CharField('Code', max_length=10)
    price = models.DecimalField('Price', default=0, decimal_places=3, max_digits=16)
    logo = models.ImageField('Logo', upload_to='uploads/', null=True, blank=True)
    update_date = models.DateTimeField('Update date', auto_now=True)
    published_date = models.DateTimeField('Create date', auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name