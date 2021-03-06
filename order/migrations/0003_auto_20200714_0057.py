# Generated by Django 3.0.8 on 2020-07-13 19:27

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200714_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
