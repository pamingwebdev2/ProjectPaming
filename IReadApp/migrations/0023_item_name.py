# Generated by Django 3.1.6 on 2021-04-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0022_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
