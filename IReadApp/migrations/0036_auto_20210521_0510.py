# Generated by Django 3.1.6 on 2021-05-21 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IReadApp', '0035_author_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateBorr', models.DateField(default='')),
                ('DueDate', models.DateField(default='')),
                ('DateRet', models.DateField(default='')),
                ('Remarks', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='DonTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCon', models.DateField(default='')),
                ('Quantity', models.IntegerField(default='')),
                ('Mode', models.TextField(default='')),
                ('DateTrans', models.DateField(default='')),
                ('Message', models.TextField(default='')),
                ('Status', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpoName', models.TextField(default='')),
                ('SpoNumber', models.TextField(default='')),
                ('SpoLocation', models.TextField(default='')),
                ('SpoAffil', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='borrowerbook',
            name='MainID',
        ),
        migrations.RemoveField(
            model_name='borrowerbook',
            name='binfo',
        ),
        migrations.RemoveField(
            model_name='brtrans',
            name='MainID',
        ),
        migrations.RemoveField(
            model_name='brtrans',
            name='binfo',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='readeroveralltrans',
            name='DateRet',
        ),
        migrations.RemoveField(
            model_name='readeroveralltrans',
            name='MainID',
        ),
        migrations.RemoveField(
            model_name='readeroveralltrans',
            name='binfo',
        ),
        migrations.RemoveField(
            model_name='retrans',
            name='DueDate',
        ),
        migrations.RemoveField(
            model_name='retrans',
            name='MainID',
        ),
        migrations.RemoveField(
            model_name='retrans',
            name='binfo',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='ReadId',
        ),
        migrations.RemoveField(
            model_name='item',
            name='MainID',
        ),
        migrations.DeleteModel(
            name='BorrowerBook',
        ),
        migrations.DeleteModel(
            name='BrTrans',
        ),
        migrations.DeleteModel(
            name='ReaderOverallTrans',
        ),
        migrations.DeleteModel(
            name='ReTrans',
        ),
        migrations.AddField(
            model_name='dontrans',
            name='sponsor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='IReadApp.sponsor'),
        ),
    ]