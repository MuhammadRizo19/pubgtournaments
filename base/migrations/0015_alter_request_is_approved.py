# Generated by Django 5.0.1 on 2024-01-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]