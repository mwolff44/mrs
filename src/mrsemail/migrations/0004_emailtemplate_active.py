# Generated by Django 2.0.3 on 2018-04-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrsemail', '0003_bichonage_verbose_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Cocher si actif'),
        ),
    ]
