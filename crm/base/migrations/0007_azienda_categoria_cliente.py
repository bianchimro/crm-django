# Generated by Django 2.0.2 on 2018-02-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20180222_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='azienda',
            name='categoria_cliente',
            field=models.CharField(blank=True, choices=[['info', 'Informatica'], ['comm', 'Commerciale'], ['edil', 'Ediliza']], max_length=20, null=True),
        ),
    ]
