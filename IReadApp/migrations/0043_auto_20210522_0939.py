# Generated by Django 3.1.6 on 2021-05-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0042_auto_20210522_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='dontrans',
            name='DateTrans',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrtrans',
            name='DateBorr',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrtrans',
            name='DateRet',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrtrans',
            name='DueDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
