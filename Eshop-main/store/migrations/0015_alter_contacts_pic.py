# Generated by Django 4.0.4 on 2022-06-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_contacts_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='pic',
            field=models.ImageField(upload_to='pic'),
        ),
    ]
