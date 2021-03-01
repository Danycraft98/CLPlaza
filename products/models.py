from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from accounts.models import User

__all__ = ['Category', 'Product', 'ProductImage', 'ProductsToBuyers', 'Tag']

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Category(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/product_images')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/'.join(str(self.image).split('/')[1:])


class ProductImage(models.Model):
    image = models.FileField(upload_to='static/product_images')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.get_image_path

    def get_image_path(self):
        return '/'.join(str(self.image).split('/')[1:])


class ProductsToBuyers(models.Model):
    quantity = models.IntegerField()
    buyers = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='buyers', on_delete=models.CASCADE)


class Tag(models.Model):
    content = models.CharField(max_length=20)
    products = models.ManyToManyField(Product, related_name='tags')

    def __str__(self):
        return self.content
