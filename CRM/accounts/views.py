from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	customers 	 = Customer.objects.all()
	orders    	 = Order.objects.all()
	total_orders = Order.objects.all().count()
	deliver_order= orders.filter(status='Delivered').count()
	pending_order= orders.filter(status='Pending').count()
	context	     = {
		'customers' : customers,
		'orders'	: orders,
		'total_orders' : total_orders,
		'deliver_order' : deliver_order,
		'pending_order' : pending_order
	}	
	return render(request,'accounts/dashboard.html',context)

def products(request):
	products = Product.objects.all()
	context  = {
		'products' :products
	}
	return render(request,'accounts/product.html',context)

def customer(request):
	return render(request,'accounts/customer.html')

