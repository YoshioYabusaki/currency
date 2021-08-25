# Generated by Django 3.2.5 on 2021-08-17 14:38

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0009_auto_20210816_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='responselog',
            name='request_method',
            field=models.CharField(choices=[('GET', 'get'), ('POST', 'post')],
                                   default=datetime.datetime(2021, 8, 17, 14, 38, 40, 406677, tzinfo=utc),
                                   max_length=4),
            preserve_default=False,
        ),
    ]