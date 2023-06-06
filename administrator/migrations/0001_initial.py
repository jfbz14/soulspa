# Generated by Django 4.1.3 on 2022-12-07 21:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDateService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=25, unique=True)),
                ('time_start', models.TimeField(help_text='HH:MM')),
                ('time_end', models.TimeField(help_text='HH:MM')),
                ('commission_limit', models.IntegerField(default=0)),
                ('condition', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=25)),
                ('document', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=25)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('city', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeHistoryBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('count_booking', models.IntegerField()),
                ('count_service', models.IntegerField()),
                ('commission_limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='None', max_length=25)),
                ('price_total', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('classsification', models.CharField(choices=[('cost', 'cost'), ('expense', 'expense')], default='expense', max_length=25)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=25)),
                ('price', models.FloatField()),
                ('assistant', models.CharField(default='None', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEmployeeBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('commission_percentage', models.FloatField()),
                ('total_commission', models.FloatField()),
                ('created', models.DateTimeField()),
                ('id_booking', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administrator.employeehistorybooking')),
            ],
        ),
    ]
