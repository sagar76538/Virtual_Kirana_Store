# Generated by Django 4.0.4 on 2022-06-04 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_password_contact_msg_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacts',
        ),
    ]
