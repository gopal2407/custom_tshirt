# Generated by Django 5.0 on 2023-12-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custome_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='minimum_amount',
            field=models.FloatField(default=0),
        ),
    ]
