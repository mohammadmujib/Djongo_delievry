# Generated by Django 3.0.8 on 2020-07-13 19:22

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mob_no',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, primary_key=True, serialize=False),
        ),
    ]
