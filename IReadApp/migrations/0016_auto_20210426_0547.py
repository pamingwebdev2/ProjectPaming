# Generated by Django 3.1.6 on 2021-04-26 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0015_auto_20210425_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='bauth',
        ),
        migrations.RemoveField(
            model_name='item',
            name='bgenre',
        ),
        migrations.RemoveField(
            model_name='item',
            name='btitle',
        ),
    ]
