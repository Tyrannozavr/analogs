# Generated by Django 4.2 on 2023-04-17 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analogs', '0002_analogs_products_analogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analogs',
            options={'verbose_name': 'Analog', 'verbose_name_plural': 'Analogs'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='analogs',
            new_name='_analogs',
        ),
    ]
