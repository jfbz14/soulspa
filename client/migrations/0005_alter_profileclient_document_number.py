# Generated by Django 4.1.3 on 2023-06-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_profileclient_document_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileclient',
            name='document_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
