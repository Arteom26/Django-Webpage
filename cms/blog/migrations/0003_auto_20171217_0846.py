# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='body',
        ),
    ]