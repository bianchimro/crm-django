# Generated by Django 2.0.2 on 2018-02-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Azienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('codice', models.CharField(max_length=30)),
                ('indirizzo', models.CharField(blank=True, max_length=200, null=True)),
                ('citta', models.CharField(blank=True, max_length=200, null=True, verbose_name='Città')),
            ],
        ),
    ]
