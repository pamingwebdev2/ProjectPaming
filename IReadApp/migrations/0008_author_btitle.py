# Generated by Django 3.1.6 on 2021-04-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0007_author_bauth'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='btitle',
            field=models.TextField(default=''),
        ),
    ]