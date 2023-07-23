from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"    

class User(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField()
    cellphone = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

