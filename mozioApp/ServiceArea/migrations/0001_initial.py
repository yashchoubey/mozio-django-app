# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitud1e', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('currency', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('language', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='providerArea_area_id', to='ServiceArea.Area')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='providerArea_provider_id', to='ServiceArea.Provider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
