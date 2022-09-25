# Generated by Django 4.0.4 on 2022-06-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_contact_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='msg',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
