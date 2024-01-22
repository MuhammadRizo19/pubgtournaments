# Generated by Django 5.0.1 on 2024-01-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_tournament_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='squad',
            field=models.CharField(choices=[('Solo', 'Solo'), ('Duo', 'Duo'), ('Squad', 'Squad')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]