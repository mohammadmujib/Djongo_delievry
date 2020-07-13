# Generated by Django 3.0.8 on 2020-07-13 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200714_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('orders', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.Order')),
                ('request', models.BooleanField(default=True)),
                ('accepted', models.BooleanField()),
                ('accepted_time', models.DateTimeField(blank=True, null=True)),
                ('arrived', models.BooleanField()),
                ('arrived_time', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.BooleanField()),
                ('delivered_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]