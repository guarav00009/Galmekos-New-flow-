from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from vehicle.models import Vehicle


class CustomVehicleCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Vehicle
        fields = ('vehicle_no','chassis_no',)

