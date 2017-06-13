# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-13 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('template', models.CharField(default='page.html', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
