# Generated by Django 3.1.6 on 2021-05-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0036_auto_20210521_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrtrans',
            name='bookId',
            field=models.ManyToManyField(default=None, to='IReadApp.Item'),
        ),
        migrations.AddField(
            model_name='borrtrans',
            name='borrId',
            field=models.ManyToManyField(default=None, to='IReadApp.Borrower'),
        ),
    ]