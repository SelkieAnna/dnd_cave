# Generated by Django 3.2.5 on 2021-07-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('characters', models.ManyToManyField(to='lore.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('characters', models.ManyToManyField(to='lore.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('characters', models.ManyToManyField(to='lore.Character')),
                ('events', models.ManyToManyField(to='lore.Event')),
                ('factions', models.ManyToManyField(to='lore.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('characters', models.ManyToManyField(to='lore.Character')),
                ('events', models.ManyToManyField(to='lore.Event')),
                ('factions', models.ManyToManyField(to='lore.Faction')),
                ('places', models.ManyToManyField(to='lore.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('characters', models.ManyToManyField(to='lore.Character')),
                ('factions', models.ManyToManyField(to='lore.Faction')),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='items',
            field=models.ManyToManyField(to='lore.Item'),
        ),
        migrations.AddField(
            model_name='faction',
            name='places',
            field=models.ManyToManyField(to='lore.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='factions',
            field=models.ManyToManyField(to='lore.Faction'),
        ),
        migrations.AddField(
            model_name='event',
            name='places',
            field=models.ManyToManyField(to='lore.Place'),
        ),
        migrations.AddField(
            model_name='character',
            name='events',
            field=models.ManyToManyField(to='lore.Event'),
        ),
        migrations.AddField(
            model_name='character',
            name='factions',
            field=models.ManyToManyField(to='lore.Faction'),
        ),
        migrations.AddField(
            model_name='character',
            name='items',
            field=models.ManyToManyField(to='lore.Item'),
        ),
        migrations.AddField(
            model_name='character',
            name='places',
            field=models.ManyToManyField(to='lore.Place'),
        ),
    ]
