# Generated by Django 3.1.6 on 2021-05-22 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0043_auto_20210522_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='penalty',
            old_name='Status',
            new_name='Query',
        ),
    ]