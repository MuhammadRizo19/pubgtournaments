# Generated by Django 5.0.1 on 2024-01-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_request_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='checked',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
