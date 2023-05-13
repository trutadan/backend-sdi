# Generated by Django 4.2 on 2023-05-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_payment_order_alter_refund_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('STUDENT', 'Moderator'), ('REGULAR', 'Regular'), ('ANONYMOUS', 'Anonymous')], db_column='role', max_length=50, null=True),
        ),
    ]