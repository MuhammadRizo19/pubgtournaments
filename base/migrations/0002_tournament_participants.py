# Generated by Django 5.0.1 on 2024-01-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='participants',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]