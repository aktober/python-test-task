# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-12 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
                ('starts_at', models.CharField(max_length=20)),
                ('ends_at', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.Company')),
            ],
            options={
                'verbose_name_plural': 'vacancies',
            },
        ),
        migrations.CreateModel(
            name='VacancyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='image_list',
            field=models.ManyToManyField(to='recruiting.VacancyImage'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='location',
            field=models.ManyToManyField(to='recruiting.City'),
        ),
    ]
