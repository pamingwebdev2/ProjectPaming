# Generated by Django 3.1.6 on 2021-05-11 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0030_borrowerbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowerbook',
            old_name='ReaderId',
            new_name='MainID',
        ),
    ]