from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User




class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_date',)


    def __str__(self):
        return self.name
    



class Employee(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Restaurant Manager'),
        ('assistant_manager', 'Assistant Manager'),
        ('chef', 'Chef'),
        ('sous_chef', 'Sous Chef'),
        ('waiter', 'Waiter/Waitress'),
        ('bartender', 'Bartender'),
        ('cashier', 'Cashier'),
        ('delivery', 'Delivery Driver'),
    ]
        
    profile = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(70)],)
    role = models.CharField(max_length=18, choices=ROLE_CHOICES)
    biography = models.TextField()
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)


    def __str__(self):
        return f"{self.name} - {self.role} - {self.phone_number}"




class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    TABLE_CHOICES = [
        ('number', '11'),
        ('number', '22'),
        ('number', '33'),
        ('number', '44'),
        ('number', '55'),
        ('number', '66'),
        ('number', '77'),
        ('number', '88'),
        ('number', '99'),
    ]
    table_number = models.CharField(max_length=6, choices=TABLE_CHOICES)
    seats = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(30)
        ]
    )
    date = models.DateField()
    time = models.TimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('not_Reserved', 'Not Reserved'),
    ]

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='not_Reserved')


    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
            return f"{self.customer} - {self.table_number} - {self.is_available} - {self.status}"