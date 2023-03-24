# Generated by Django 4.1.3 on 2022-12-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2022-12-21 11:37:36', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='imageURL',
            field=models.CharField(default='/auctions/templates/auctions/images/qMark.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2022-12-21 11:37:36', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(default=None),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoTitle', models.CharField(max_length=280)),
                ('videoLink', models.CharField(max_length=200)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.section')),
            ],
        ),
    ]
