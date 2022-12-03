
from django.db import models

class Customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phno=models.CharField(max_length=12)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()
    def check_email(self):
        if(Customer.objects.filter(email=self.email)):
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.fname