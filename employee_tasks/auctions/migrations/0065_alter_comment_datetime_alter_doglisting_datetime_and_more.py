# Generated by Django 4.1.3 on 2023-04-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0064_alter_comment_datetime_alter_doglisting_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default='2023-04-07 11:47:54', max_length=100),
        ),
        migrations.AlterField(
            model_name='doglisting',
            name='datetime',
            field=models.CharField(default='11:47:54 04-07-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.DateTimeField(default='2023-04-07 11:47:54', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeelisting',
            name='datetime',
            field=models.CharField(default='11:47:54 EST, 04-07-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='11:47:54 04-07-2023', max_length=100),
        ),
    ]
