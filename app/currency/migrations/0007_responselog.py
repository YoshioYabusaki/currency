# Generated by Django 3.2.5 on 2021-08-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_remove_contactus_email_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.PositiveSmallIntegerField()),
                ('path', models.CharField(max_length=255)),
                ('response_time', models.PositiveSmallIntegerField()),
            ],
        ),
    ]