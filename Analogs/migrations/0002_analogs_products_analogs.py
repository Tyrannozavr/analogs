# Generated by Django 4.2 on 2023-04-17 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Analogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='analogs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Analogs.analogs'),
        ),
    ]
