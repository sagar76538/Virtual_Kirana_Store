# Generated by Django 4.0.4 on 2022-06-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_contacts_email_alter_contacts_msg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='pic',
            field=models.ImageField(default=None, upload_to='pic'),
        ),
    ]
