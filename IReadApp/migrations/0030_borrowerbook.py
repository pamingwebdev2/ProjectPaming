# Generated by Django 3.1.6 on 2021-05-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0029_auto_20210509_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowerBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReaderId', models.ManyToManyField(default=None, to='IReadApp.Borrower')),
                ('binfo', models.ManyToManyField(default=None, to='IReadApp.Item')),
            ],
        ),
    ]
