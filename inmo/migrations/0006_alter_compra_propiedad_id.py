# Generated by Django 4.0.5 on 2022-06-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmo', '0005_alter_compra_propiedad_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='propiedad_id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
