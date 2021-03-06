# Generated by Django 2.0 on 2018-01-13 11:20

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mrsattachment', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('mrsattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mrsattachment.MRSAttachment')),
            ],
            options={
                'verbose_name': 'Justificatif',
                'ordering': ['mrsrequest', 'id'],
            },
            bases=('mrsattachment.mrsattachment',),
        ),
        migrations.CreateModel(
            name='MRSRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('form_id', models.CharField(max_length=12, unique=True, verbose_name='Identifiant de formulaire')),
                ('creation_datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name="Date et heure d'enregistrement du formulaire")),
                ('distance', models.PositiveIntegerField(help_text='Kilométrage total parcouru', null=True, verbose_name='Distance (km)')),
                ('expense', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Parking et/ou péage ou justificatif(s) de transport en commun', max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Montant total des frais (en € TTC)')),
                ('status', models.IntegerField(choices=[(0, 'Soumise'), (1, 'Validée'), (2, 'Rejettée')], default=0)),
                ('insured', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.Person')),
            ],
            options={
                'verbose_name': 'Requête',
                'ordering': ['-creation_datetime'],
            },
        ),
        migrations.CreateModel(
            name='PMT',
            fields=[
                ('mrsattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mrsattachment.MRSAttachment')),
                ('mrsrequest', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest')),
            ],
            options={
                'ordering': ['mrsrequest', 'id'],
            },
            bases=('mrsattachment.mrsattachment',),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateField(help_text='Date du trajet aller', null=True, verbose_name='Aller')),
                ('date_return', models.DateField(help_text='Date du trajet retour', null=True, verbose_name='Retour')),
                ('mrsrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest')),
            ],
            options={
                'ordering': ['mrsrequest'],
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='mrsrequest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest'),
        ),
    ]
