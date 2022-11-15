from django.db import models
STATUS_CHOICES = [('other', 'Raznoe'), ('fruits', 'Fruits'), ('vegs', 'Vegs'), ('bakery', 'Bakery'), ('milk', 'Milk')]
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Naimenovanie tovara')
    content = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Opisanie tovara')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='other', verbose_name='Status')
    balance = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

def __str__(self):
    return f'{self.id}. {self.title}'