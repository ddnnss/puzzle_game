# Generated by Django 2.2.7 on 2020-05-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_auto_20200518_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
    ]