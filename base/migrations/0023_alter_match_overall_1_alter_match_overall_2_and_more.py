# Generated by Django 5.0.1 on 2024-03-04 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_match_overall_1_match_overall_2_match_winner_and_more'),
        ('user', '0008_minuspoint_reason_point_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='overall_1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='overall_2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]