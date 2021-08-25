# Generated by Django 3.2.5 on 2021-08-16 13:52

from currency import model_choices as mch

from django.db import migrations


# from currency.models import Rate  # WRONG


def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    for rate in Rate.objects.all().only('type'):
        if 'uds' in rate.type.lower():
            rate.type = mch.TYPE_USD
        elif 'eur' in rate.type.lower():
            rate.type = mch.TYPE_EUR
        else:
            rate.type = mch.TYPE_USD

        rate.save(update_fields=('type', ))


def backwards(apps, schema_editor):
    pass
    # print('backwards \n' * 10)


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_auto_20210816_1347'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]