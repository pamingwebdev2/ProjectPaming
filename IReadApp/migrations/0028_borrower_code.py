# Generated by Django 3.1.6 on 2021-05-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0027_auto_20210502_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='code',
            field=models.TextField(default=''),
        ),
    ]
