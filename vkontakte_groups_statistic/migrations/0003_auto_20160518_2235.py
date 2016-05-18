# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_groups_statistic', '0002_auto_20160518_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupstat',
            name='reach_ads',
            field=models.PositiveIntegerField(null=True, verbose_name='\u0420\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0439 \u043e\u0445\u0432\u0430\u0442'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupstat',
            name='reach_viral',
            field=models.PositiveIntegerField(null=True, verbose_name='\u0412\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0445\u0432\u0430\u0442'),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='groupstat',
            table=None,
        ),
        migrations.AlterModelTable(
            name='groupstatistic',
            table=None,
        ),
        migrations.AlterModelTable(
            name='groupstatpercentage',
            table=None,
        ),
    ]
