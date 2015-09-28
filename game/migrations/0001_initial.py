# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_blue', models.BooleanField(default=True)),
                ('guesses_allowed', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('word', models.CharField(max_length=50, default=None)),
                ('selected', models.BooleanField(default=False)),
                ('card_type', models.CharField(choices=[('bl', 'Blue Team'), ('rd', 'Red Team'), ('bg', 'Bystander'), ('bk', 'Assassin')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('clue', models.CharField(max_length=50, default=None)),
                ('num_of_cards', models.PositiveSmallIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary_Words',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('list_of_words', models.TextField(max_length=50, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('is_blue', models.BooleanField(primary_key=True, serialize=False, default=True)),
                ('spies_left', models.PositiveSmallIntegerField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='clue',
            name='team',
            field=models.ForeignKey(to='game.Team'),
        ),
        migrations.AddField(
            model_name='board',
            name='active_team',
            field=models.ForeignKey(to='game.Team', default=None),
        ),
    ]
