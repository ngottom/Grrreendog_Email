# Generated by Django 4.1.3 on 2023-01-27 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0047_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeelisting',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2023-01-27 13:18:50', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2023-01-27 13:18:50', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='13:18:50 01-27-2023', max_length=100),
        ),
    ]
