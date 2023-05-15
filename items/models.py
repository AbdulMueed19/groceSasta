from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null = True ,blank = True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_image')
    created_by = models.ForeignKey(User,on_delete= models.CASCADE,related_name='items')
    category = models.ForeignKey(Category,on_delete= models.CASCADE,related_name='items')
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Items"
        ordering = ('name',)

    def __str__(self):
        return self.name