# Generated by Django 2.2.7 on 2020-05-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_user_last_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=50, null=True, verbose_name='Логин'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, null=True, verbose_name='Ник'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='user',
            name='study',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Эл. почта'),
        ),
    ]