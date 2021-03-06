# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-18 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u6559\u5e08\u7ba1\u7406', 'verbose_name_plural': '\u6559\u5e08\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '\u57f9\u8bad\u673a\u6784'), ('gr', '\u4e2a\u4eba'), ('gx', '\u9ad8\u6821')], default='\u57f9\u8bad\u673a\u6784', max_length=20, verbose_name='\u673a\u6784\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='Logo'),
        ),
    ]
