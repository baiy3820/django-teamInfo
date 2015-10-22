# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_reason', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teamer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english_name', models.CharField(max_length=64)),
                ('Chinese_name', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=8)),
                ('Birthday', models.DateTimeField(verbose_name=b'Birthday')),
                ('phone', models.CharField(max_length=64)),
                ('hobby', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=64)),
                ('dayily_voice', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='teamer',
            field=models.ForeignKey(to='teamInfo.Teamer'),
        ),
    ]
