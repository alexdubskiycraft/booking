from django.db import models
from django.utils import timezone

class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    role = models.CharField(max_length=20, db_default='user')

    def __str__(self):
        return self.lastname
    

class Room(models.Model):
    number = models.IntegerField()
    room_type = models.CharField(max_length=50)
    enabled = models.IntegerField()
    count_bed = models.IntegerField()
    floor = models.IntegerField()
    bar = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.number)   
    
class Booking(models.Model):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='books', on_delete=models.CASCADE)   
    begin_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    




