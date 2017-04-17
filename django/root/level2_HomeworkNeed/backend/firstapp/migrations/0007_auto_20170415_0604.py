# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20170415_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('like', 'like'), ('dislike', 'dislike')], max_length=10),
        ),
    ]