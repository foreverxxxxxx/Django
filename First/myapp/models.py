from django.db import models
from django.utils.text import slugify
# https://docs.djangoproject.com/en/5.0/topics/db/models/
#https://docs.djangoproject.com/en/5.0/topics/db/queries/
# Create your models here.

class Category(models.Model):
   name=models.CharField(max_length=100)
   def __str__(self):
    return self.name 

class Address(models.Model):
  street=models.CharField(max_length=100)
  postal_code=models.CharField(max_length=5)
  city=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.street} {self.postal_code} {self.city}"

class Supplier(models.Model):
  company_name=models.CharField(max_length=100)
  address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

  def __str__(self):
      return self.company_name
  



class Product(models.Model):
   name=models.CharField(max_length=50)
   price=models.DecimalField(max_digits=8,decimal_places=2)
   description=models.CharField(max_length=200)
   imageUrl=models.CharField(max_length=50)
   isActive=models.BooleanField(default=False)
   #category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name="products")       #models.CharField(max_length=8,null=True)
   slug=models.SlugField(default="",blank=False,null=False,db_index=True,unique=True)
   categories=models.ManyToManyField(Category)
   supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)

   # def save(self, *args,**kargs):
   #    self.slug= slugify(self.name)
   #    super().save(args, kargs)

   def __str__(self):
     return f"{self.name}  {self.price} {self.slug}"
   