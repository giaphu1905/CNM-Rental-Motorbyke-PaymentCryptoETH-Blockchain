# Generated by Django 5.0.6 on 2024-05-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0014_orderphukien_order_phu_phi'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_baohiem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_diduongdai',
            field=models.BooleanField(default=False),
        ),
    ]