# Generated by Django 4.2 on 2023-04-22 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(db_column='order_number', on_delete=django.db.models.deletion.CASCADE, to='api.order'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='order',
            field=models.OneToOneField(blank=True, db_column='order_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order'),
        ),
    ]
