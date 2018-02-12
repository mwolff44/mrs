# Generated by Django 2.0.2 on 2018-02-09 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
        ('mrsrequest', '0006_form_id_to_display_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrsrequest',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.Institution'),
        ),
    ]