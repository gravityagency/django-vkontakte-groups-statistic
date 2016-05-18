# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_groups_statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupstat',
            name='activity_product_comments',
            field=models.PositiveIntegerField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043a \u0442\u043e\u0432\u0430\u0440\u0430\u043c'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupstat',
            name='section_products',
            field=models.PositiveIntegerField(null=True, verbose_name='\u0422\u043e\u0432\u0430\u0440\u044b'),
            preserve_default=True,
        ),
    ]
