from django.db import models
from django.utils import timezone
# Create your models here.
class Elevator(models.Model):
    name = models.CharField(max_length=50)
    current_floor = models.IntegerField(default=0)
    max_floor = models.IntegerField()
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ElevatorRequest(models.Model):
    elevator= models.IntegerField()
    request_floor = models.IntegerField()
    request_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        elevator_name = Elevator.objects.filter(id=self.elevator).first()
        return elevator_name