# Generated by Django 4.2 on 2025-02-09 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_address_remove_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
