# Generated by Django 2.0.1 on 2018-02-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrsrequest', '0004_misc'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrsrequest',
            name='creation_ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
