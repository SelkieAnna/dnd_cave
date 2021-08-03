# Generated by Django 3.2.5 on 2021-07-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='faction',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='mood_media_link',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
