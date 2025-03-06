from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    # required=True
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Price")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    material = models.TextField()
    is_available = models.BooleanField(default=False)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    



class Order(models.Model):
    phone_number = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        total_items = self.items.count()
        return f"Order {self.id} by {self.phone_number.phone_number} (Total Items: {total_items})"
    

        
    def total_price(self):
        return sum(order_item.item.price * order_item.quantity for order_item in self.orderitem_set.all())  # جمع زدن قیمت آیتم‌ها با توجه به تعداد
 
    


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Order.objects.create(phone_number=instance) 
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} (x{self.quantity})"
    
