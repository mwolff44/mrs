# Generated by Django 2.0.3 on 2018-03-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
