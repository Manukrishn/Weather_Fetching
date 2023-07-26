# Generated by Django 4.2.2 on 2023-07-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weather_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather_check',
            name='icon',
            field=models.FileField(default=None, null=True, upload_to='static/icons'),
        ),
        migrations.AddField(
            model_name='weather_check',
            name='main',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weather_check',
            name='temperature',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='weather_check',
            name='Location',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]