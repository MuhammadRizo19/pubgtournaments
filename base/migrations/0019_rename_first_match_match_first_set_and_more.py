# Generated by Django 5.0.1 on 2024-03-02 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_request_checked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='first_match',
            new_name='first_set',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='second_match',
            new_name='second_set',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='third_match',
            new_name='third_set',
        ),
    ]
