# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Distrat_ma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('f_name', models.CharField(db_column='f_name', max_length=25)),
                ('l_name', models.CharField(db_column='l_name', max_length=25)),
                ('avis_text', models.CharField(db_column='avis_text', max_length=500)),
                ('dt_created', models.DateTimeField(db_column='dt_created')),
            ],
            options={
                'db_table': 'avis',
                'managed': False,
            },
        ),
    ]
