# Generated by Django 2.2.5 on 2021-06-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0005_auto_20210620_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmail',
            name='send_on',
            field=models.DateTimeField(),
        ),
    ]
