# Generated by Django 5.0.1 on 2024-03-02 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_rename_first_match_match_first_set_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='first_set',
        ),
        migrations.RemoveField(
            model_name='match',
            name='second_set',
        ),
        migrations.RemoveField(
            model_name='match',
            name='third_set',
        ),
    ]
