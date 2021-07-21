from django.db import models
from EcommerceProject.models import UserProfile
from seller.models import Product
# Create your models here.
class Cart(models.Model):
	#Composite Unique Key
	class Meta():
			unique_together = ('users', 'product')
	users = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
	
class AddressDetail(models.Model):
	add_line1 = models.CharField(max_length=100)
	add_line2 = models.CharField(max_length=100)
	pincode = models.IntegerField()
	city = models.CharField(max_length=100)
	landmark = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	mobile = models.CharField(max_length=20)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Orders(models.Model):
	order_id = models.CharField(max_length=100) #OD_16052021_RANDOMNUM
	order_date = models.DateTimeField(auto_now=True)
	total_amt = models.DecimalField(max_digits=10, decimal_places=2)
	amt_status = models.IntegerField(default=0) #0-->Unpaid
	order_status = models.IntegerField(default=0) #0-->Placed
	placedby = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	address = models.ForeignKey(AddressDetail, on_delete=models.CASCADE)

class OrderProduct(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.IntegerField()
	status = models.IntegerField(default=0) #0->placedbyd

class WishList(models.Model):
	#Composite Unique Key
	class Meta():
			unique_together = ('user', 'product')
	user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)