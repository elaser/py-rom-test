# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('lat', models.DecimalField(default=Decimal('0.0'), max_digits=15, decimal_places=10)),
                ('lng', models.DecimalField(default=Decimal('0.0'), max_digits=15, decimal_places=10)),
                ('email', models.EmailField(unique=True, max_length=255, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
