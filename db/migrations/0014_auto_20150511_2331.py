# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_auto_20150506_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condiciones',
            name='found_payment',
        ),
        migrations.RemoveField(
            model_name='condiciones',
            name='found_trust',
        ),
    ]
