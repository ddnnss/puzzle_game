# Generated by Django 2.2.7 on 2020-05-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20200516_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='game_images/')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='last_image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]