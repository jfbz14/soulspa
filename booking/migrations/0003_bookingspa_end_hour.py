# Generated by Django 4.1.3 on 2022-12-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_bookingspa_service_bookingspa_time_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingspa',
            name='end_hour',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]