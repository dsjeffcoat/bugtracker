# Generated by Django 3.1 on 2020-08-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='display_name',
        ),
    ]
