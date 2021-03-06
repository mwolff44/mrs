# Generated by Django 2.0.2 on 2018-02-07 01:09

from django.conf import settings
from django.db import migrations, models
from django.db.models.functions import Length


def provision_display_id(apps, schema_editor):
    MRSRequest = apps.get_model('mrsrequest', 'MRSRequest')

    def exists():
        return MRSRequest.objects.exclude(
            pk=instance.pk).filter(display_id=instance.display_id)

    instances = MRSRequest.objects.annotate(
        form_id_length=Length('form_id')
    ).filter(form_id_length=12)

    for instance in instances:
        instance.display_id = instance.form_id
        while exists():
            instance.display_id += 1
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mrsrequest', '0005_mrsrequest_creation_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrsrequest',
            name='display_id',
            field=models.BigIntegerField(null=True, verbose_name='Numéro de demande'),
            preserve_default=False,
        ),
        migrations.RunPython(provision_display_id),
        migrations.AlterField(
            model_name='mrsrequest',
            name='display_id',
            field=models.BigIntegerField(unique=True, verbose_name='Numéro de demande'),
        ),
        migrations.RemoveField(
            model_name='mrsrequest',
            name='form_id',
        ),
    ]

    if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql':
        operations.append(migrations.RunSQL('''
        DROP TRIGGER IF EXISTS mrsrequest_formid_trigger ON mrsrequest_mrsrequest;
        DROP FUNCTION IF EXISTS mrsrequest_formid_seq_increment CASCADE;
        DROP TABLE IF EXISTS mrsrequest_formid;
        '''))
