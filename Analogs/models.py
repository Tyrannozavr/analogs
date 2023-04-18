from django.db import models

class Analogs(models.Model):
    class Meta:
        verbose_name = 'Analog'
        verbose_name_plural = 'Analogs'

    def __str__(self):
        return ', '. join([product.name for product in self.products_set.all()[:5]])

class Products(models.Model):
    name = models.CharField(max_length=20)
    analogs = models.ForeignKey(Analogs, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField()
    products = models.ManyToManyField(Products)