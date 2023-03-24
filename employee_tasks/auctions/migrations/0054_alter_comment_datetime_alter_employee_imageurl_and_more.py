# Generated by Django 4.1.3 on 2023-01-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0053_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2023-01-27 14:14:25', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='imageURL',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/800px-Question_mark_%28black%29.svg.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2023-01-27 14:14:25', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeelisting',
            name='datetime',
            field=models.CharField(default='14:14:25 EST, 01-27-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='14:14:25 01-27-2023', max_length=100),
        ),
    ]