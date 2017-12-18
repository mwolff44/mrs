# Generated by Django 2.0 on 2017-12-18 09:58

from django.db import migrations, models
import django.db.models.deletion
import mrsattachment.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mrsrequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name="Heure d'enregistrement du fichier")),
                ('binary', mrsattachment.models.MRSAttachmentField(verbose_name='Prescription Médicale de Transport')),
                ('mrsrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest')),
            ],
            options={
                'ordering': ['mrsrequest', 'id'],
            },
        ),
    ]
