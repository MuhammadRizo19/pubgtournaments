# Generated by Django 5.0.1 on 2024-01-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_points_profile_pubg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]