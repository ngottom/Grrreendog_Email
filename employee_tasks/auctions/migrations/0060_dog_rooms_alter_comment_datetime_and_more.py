# Generated by Django 4.1.3 on 2023-02-25 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0059_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('breed', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=False)),
                ('imageURL', models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/800px-Question_mark_%28black%29.svg.png', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='02-25-2023 10:55:28', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='02-25-2023 10:55:28', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeelisting',
            name='datetime',
            field=models.CharField(default='10:55:28 EST, 02-25-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='10:55:28 02-25-2023', max_length=100),
        ),
        migrations.CreateModel(
            name='dogListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(default='10:55:28 02-25-2023', max_length=100)),
                ('dog', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogAuthor', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roomName', to='auctions.rooms')),
            ],
        ),
    ]
