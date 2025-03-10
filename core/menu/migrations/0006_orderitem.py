# Generated by Django 4.2 on 2025-02-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.order')),
            ],
        ),
    ]
