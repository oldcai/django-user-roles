# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-26 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userroles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='name',
            field=models.CharField(choices=[('user_inactive', 'user_inactive'), ('enterprise', 'enterprise'), ('user', 'user'), ('vip', 'vip'), ('trial', 'trial'), ('new_user', 'new_user'), ('premium', 'premium')], max_length=100),
        ),
    ]
