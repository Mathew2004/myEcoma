# Generated by Django 4.2.4 on 2023-08-13 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
