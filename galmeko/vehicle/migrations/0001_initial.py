# Generated by Django 2.2 on 2020-01-25 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=25, unique=True)),
                ('mileage', models.CharField(max_length=11)),
                ('chassis_no', models.CharField(max_length=20)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Booked'), (3, 'Deleted')], default=1, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
    ]