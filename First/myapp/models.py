from django.db import models
from django.utils.text import slugify
# https://docs.djangoproject.com/en/5.0/topics/db/models/
#https://docs.djangoproject.com/en/5.0/topics/db/queries/
# Create your models here.
class Product(models.Model):
   name=models.CharField(max_length=50)
   price=models.DecimalField(max_digits=8,decimal_places=2)
   description=models.CharField(max_length=200)
   imageUrl=models.CharField(max_length=50)
   isActive=models.BooleanField(default=False)
   category=models.CharField(max_length=8,null=True)
   slug=models.SlugField(default="",blank=False,editable=False,null=False,db_index=True,unique=True)

   def save(self, *args,**kargs):
      self.slug= slugify(self.name)
      super().save(args, kargs)

   def __str__(self):
     return f"{self.name}  {self.price} {self.slug}"
   