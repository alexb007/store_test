# Generated by Django 2.2.3 on 2019-08-03 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, verbose_name='Order Name')),
                ('status', models.CharField(choices=[('inprogress', 'In Progress'), ('packaging', 'Packaging'), ('shipped', 'Shipped'), ('canceled', 'Canceled')], default='inprogress', max_length=12, verbose_name='Order Status')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
            },
        ),
    ]
