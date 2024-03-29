# Generated by Django 5.0.1 on 2024-01-23 05:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tournament_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('round_number', models.CharField(max_length=35)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tournament')),
            ],
        ),
    ]
