# Generated by Django 5.0.6 on 2024-06-12 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_loaction_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='loaction',
            new_name='location',
        ),
    ]
