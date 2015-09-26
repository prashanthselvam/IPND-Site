# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbookpost',
            name='text',
            field=models.TextField(default=datetime.datetime(2015, 9, 26, 8, 48, 30, 633000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
