# Generated by Django 5.0.1 on 2024-01-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='started',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
