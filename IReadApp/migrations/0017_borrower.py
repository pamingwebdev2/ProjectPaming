# Generated by Django 3.1.6 on 2021-04-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0016_auto_20210426_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
