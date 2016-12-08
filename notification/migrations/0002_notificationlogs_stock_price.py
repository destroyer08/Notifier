# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationlogs',
            name='stock_price',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
