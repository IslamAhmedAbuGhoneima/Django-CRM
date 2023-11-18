from django.db import models

# Create your models here.
class Record(models.Model):
    created = models.DateField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

