# Generated by Django 4.1.2 on 2022-11-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_comment_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2022-11-20 11:53:26', max_length=100),
        ),
    ]