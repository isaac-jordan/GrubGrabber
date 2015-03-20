# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('grubgrabber', '0003_auto_20150319_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='name',
            field=models.CharField(default='MISSING', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dislike',
            name='name',
            field=models.CharField(default='MISSING', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favourite',
            name='name',
            field=models.CharField(default='MISSING', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
