# Generated by Django 3.1.6 on 2021-04-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0006_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bauth',
            field=models.TextField(default=''),
        ),
    ]
