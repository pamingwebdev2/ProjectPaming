# Generated by Django 3.1.6 on 2021-04-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]