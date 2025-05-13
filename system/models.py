from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    

Destination_Choices = (
    ("GIKI","GIKI"),
    ("Peshawar","Peshawar"),
    ("Abbotabad","Abbotabad"),
    ("Pindi","Pindi"),
    ("Islamabad","Islamabad"),
    ("Lahore","Lahore")
)
class driver(models.Model):
    driver_name = models.CharField(max_length=30)
    driver_number = models.IntegerField()

    def __str__(self) -> str:
        return self.driver_name

class destination(models.Model):
    from_destination = models.CharField(max_length=20,choices=Destination_Choices)
    to_destination = models.CharField(max_length=20,choices=Destination_Choices)
    bus_No = models.IntegerField()
    date =models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False) 
    bus_location = models.CharField(max_length=100)
    tickets = models.IntegerField(default=30)
    bus_driver = models.ForeignKey(driver,on_delete=models.CASCADE)
    price = models.IntegerField(default=300)
    def __str__(self) -> str:
        return self.from_destination+ "-" + self.to_destination

class ticket(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE)
    dest_pk = models.ForeignKey(destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket of {self.user_pk.username} for {self.dest_pk}"

