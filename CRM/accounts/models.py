from django.db import models

# Create your models here.
class Customer(models.Model):
	name  		= models.CharField(max_length=100, null=True)
	phone 		= models.CharField(max_length=100, null=True)
	email 		= models.EmailField()
	date_create = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name 		= 'Customer'
		verbose_name_plural = 'Customers'

class Product(models.Model):
	CATEGORY  = {

		('Indoor','Indoor'),
		('Out door','Out door'),
	}

	name 		= models.CharField(max_length=100, null=True)
	category 	= models.CharField(max_length=100,null=True, choices=CATEGORY)
	price 		= models.FloatField(null=True)
	description = models.TextField()
	date_create = models.DateTimeField(auto_now_add=True,null=True)	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name 		= 'Product'
		verbose_name_plural = 'Products'
		

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):

	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)	
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	class Meta:
		verbose_name 		= 'Order'
		verbose_name_plural = 'Orders'