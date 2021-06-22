# Generated by Django 2.2.5 on 2021-06-19 19:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('schoolname', models.CharField(max_length=1000)),
                ('contactnumber', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format:Up to 10 digits allowed.', regex='^\\d{10,10}$')])),
                ('type_user', models.CharField(choices=[('SMC Member', 'SMC Member'), ('grievance', 'grievance')], default='student', max_length=20)),
                ('schoolid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guser', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200, null=True)),
                ('Type_of_complaint', models.CharField(choices=[('Infrastructure', 'Infrastructure'), ('Human Resources', 'Human Resources'), ('Management', 'Management'), ('Other', 'Other')], max_length=200, null=True)),
                ('Receiver', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=4000, null=True)),
                ('Time', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Solved'), (2, 'InProgress'), (3, 'Pending')], default=3)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]