# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0015_auto_20170404_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystatus',
            name='notification_message',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
