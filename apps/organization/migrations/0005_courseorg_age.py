# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='age',
            field=models.IntegerField(default=18, verbose_name='\u5e74\u9f84'),
        ),
    ]
