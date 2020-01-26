from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Vehicle(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=25,unique=True)
    mileage = models.CharField(max_length=11,blank=False,null=False)
    chassis_no = models.CharField(max_length=20,blank=False,null=False)
    STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive'),
        (2, 'Booked'),
        (3, 'Deleted'),

    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_no