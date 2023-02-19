from django.db import models


class Warehouse(models.Model):
    """A class that represents a warehouse with storage availability"""
    warehouse = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    total_capacity = models.PositiveIntegerField()
    capacity_occupied = models.PositiveIntegerField()
    capacity_available = models.PositiveIntegerField()
    temperature_control = models.BooleanField()
    last_updated = models.DateField()


