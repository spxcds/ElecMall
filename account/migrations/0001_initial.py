# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Nickname', models.CharField(max_length=30)),
                ('Telephone', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
