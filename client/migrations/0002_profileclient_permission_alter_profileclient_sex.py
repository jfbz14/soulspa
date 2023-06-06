# Generated by Django 4.1.3 on 2023-01-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileclient',
            name='permission',
            field=models.CharField(choices=[('YES', 'YES'), ('NOT', 'NOT')], default='NOT', max_length=10),
        ),
        migrations.AlterField(
            model_name='profileclient',
            name='sex',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE'), ('UN', 'UNKNOWN')], default='UNKNOWN', max_length=10),
        ),
    ]