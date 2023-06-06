# Generated by Django 4.1.3 on 2022-12-01 03:10

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificatioSupplie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_area', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_distributor', models.CharField(max_length=50, unique=True)),
                ('document', models.CharField(max_length=50, unique=True)),
                ('name_contact', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomSpa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('stretcher', models.CharField(max_length=50)),
                ('condition', models.BooleanField(default=True)),
                ('positon', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50, unique=True)),
                ('unit', models.CharField(choices=[('und', 'und'), ('g', 'g'), ('ml', 'ml')], max_length=3)),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('price_unit', models.FloatField(blank=True, null=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.classificatiosupplie')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='OutCellar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=50)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.supplie')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCleaningRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=25, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.supplie')),
                ('roomspa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.roomspa')),
            ],
        ),
        migrations.CreateModel(
            name='InCellar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=50)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.supplie')),
            ],
        ),
        migrations.CreateModel(
            name='CellarGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_cellar', models.FloatField(blank=True, null=True)),
                ('out_cellar', models.FloatField(blank=True, null=True)),
                ('in_cellar_balance', models.FloatField(default=0)),
                ('difference', models.FloatField(blank=True, null=True)),
                ('cellar', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='inventory.supplie')),
            ],
        ),
    ]