# Generated by Django 4.1.3 on 2022-12-07 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('profile_user', '0002_alter_user_email'),
        ('inventory', '0002_itemcleaningroom_price_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingSpa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=25)),
                ('discount', models.IntegerField(default=0)),
                ('advance_price', models.FloatField(default=0)),
                ('balance', models.FloatField(blank=True, default=0, null=True)),
                ('position', models.CharField(choices=[('Active', 'Active'), ('Cancel', 'Cancel'), ('Finalized', 'Finalized'), ('Wait', 'Wait')], default='Wait', max_length=25)),
                ('description', models.CharField(blank=True, default='None', help_text='Enter the reason, \n Minimum 10 characters. \n Maximum 50 characters.', max_length=50, null=True)),
                ('created', models.DateTimeField()),
                ('active', models.DateTimeField(blank=True, null=True)),
                ('end_booking', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(blank=True, default=0, null=True)),
                ('condition_pay', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.profileclient')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profile_user.profileuser')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.roomspa')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=50)),
                ('time_minutes', models.IntegerField()),
                ('price', models.FloatField()),
                ('commission_percentage', models.FloatField()),
                ('position', models.CharField(choices=[('Active', 'Active'), ('Cancel', 'Cancel')], default='Active', max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bookingspa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.bookingspa')),
            ],
        ),
    ]