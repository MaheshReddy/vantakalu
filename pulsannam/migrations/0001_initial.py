# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IsrImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='IsrPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IsrPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='isrphase',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulsannam.IsrPlatform'),
        ),
        migrations.AddField(
            model_name='isrphase',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulsannam.IsrImage'),
        ),
    ]
