# Generated by Django 2.2.5 on 2021-06-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0002_auto_20210620_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='schoolid',
            field=models.CharField(max_length=20),
        ),
    ]
