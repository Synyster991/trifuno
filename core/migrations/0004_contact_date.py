# Generated by Django 3.1.5 on 2021-01-16 00:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]