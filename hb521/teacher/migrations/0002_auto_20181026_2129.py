# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('add_time', models.DateField(auto_now=True)),
                ('content', models.TextField(verbose_name=30)),
            ],
        ),
        migrations.AlterField(
            model_name='t_ser',
            name='age',
            field=models.CharField(max_length=50),
        ),
    ]
